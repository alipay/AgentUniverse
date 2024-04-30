# !/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time    : 2024/3/18 10:42
# @Author  : heji
# @Email   : lc299034@antgroup.com
# @FileName: executing_planner.py
"""Execution planner module."""
import asyncio

from langchain.chains import LLMChain
from langchain_core.memory import BaseMemory

from agentuniverse.agent.agent_model import AgentModel
from agentuniverse.agent.input_object import InputObject
from agentuniverse.agent.plan.planner.planner import Planner
from agentuniverse.base.util.prompt_util import process_llm_token
from agentuniverse.llm.llm import LLM
from agentuniverse.prompt.prompt import Prompt
from agentuniverse.prompt.prompt_manager import PromptManager
from agentuniverse.prompt.prompt_model import AgentPromptModel


class ExecutingPlanner(Planner):
    """Executing planner class."""

    def invoke(self, agent_model: AgentModel, planner_input: dict, input_object: InputObject) -> dict:
        """Invoke the planner.

        Args:
            agent_model (AgentModel): Agent model object.
            planner_input (dict): Planner input object.
            input_object (InputObject): Agent input object.
        Returns:
            dict: The planner result.
        """

        memory: BaseMemory = self.handle_memory(agent_model, planner_input)

        self.handle_action(agent_model, planner_input, input_object)

        llm: LLM = self.handle_llm(agent_model)

        prompt: Prompt = self.handle_prompt(agent_model, planner_input)

        llm_chain = LLMChain(llm=llm.as_langchain(),
                             prompt=prompt.as_langchain(),
                             output_key=self.output_key, memory=memory)
        return asyncio.run(llm_chain.acall(inputs=planner_input))

    def handle_prompt(self, agent_model: AgentModel, planner_input: dict) -> Prompt:
        """Prompt module processing.

        Args:
            agent_model (AgentModel): Agent model object.
            planner_input (dict): Planner input object.
        Returns:
            Prompt: The prompt instance.
        """
        expert_framework = planner_input.pop('expert_framework', '') or ''

        profile: dict = agent_model.profile

        origin_instruction = profile.get('instruction')
        user_instruction = expert_framework + origin_instruction if origin_instruction else origin_instruction

        user_prompt_model: AgentPromptModel = AgentPromptModel(introduction=profile.get('introduction'),
                                                               target=profile.get('target'),
                                                               instruction=user_instruction)

        # get the prompt by the prompt version
        prompt_version: str = profile.get('prompt_version') or 'executing_planner.default_cn'
        prompt: Prompt = PromptManager().get_instance_obj(prompt_version)

        system_prompt_model: AgentPromptModel = AgentPromptModel(introduction=prompt.introduction,
                                                                 target=prompt.target,
                                                                 instruction=expert_framework + prompt.instruction)

        prompt: Prompt = Prompt().build_prompt(user_prompt_model, system_prompt_model,
                                               self.prompt_assemble_order)
        process_llm_token(prompt.as_langchain(), profile, planner_input)
        return prompt
