# !/usr/bin/env python3
# -*- coding:utf-8 -*-

# @Time    : 2024/4/16 20:30
# @Author  : wangchongshi
# @Email   : wangchongshi.wcs@antgroup.com
# @FileName: test_expressing_agent.py
import unittest

from agentuniverse.agent.agent import Agent
from agentuniverse.agent.agent_manager import AgentManager
from agentuniverse.agent.input_object import InputObject
from agentuniverse.agent.output_object import OutputObject
from agentuniverse.base.agentuniverse import AgentUniverse


class ExpressingAgentTest(unittest.TestCase):
    """Test cases for the expressing agent"""

    def setUp(self) -> None:
        AgentUniverse().start(config_path='../../config/config.toml')

    def test_expressing_agent(self):
        """Test demo expressing agent.

        In the normal process, we need to generate answers to the framework questions through the executing agent.
        After that, aggregate information through the expressing agent to generate a complete answer.
        In the current demo test method, we mock answers generated by the executing Agent.
        """

        instance: Agent = AgentManager().get_instance_obj('demo_expressing_agent')

        output1 = """
         巴菲特通过其公司伯克希尔·哈撒韦自2022年开始减持比亚迪股份，具体情况如下：

        1. 2022年8月24日：伯克希尔·哈撒韦减持了133.10万股比亚迪H股，减持的均价为277.10港元，此次减持后，持股数量降至2.18719亿股。
        
        2. 2023年3月31日：伯克希尔·哈撒韦再次减持，此次为248.05万股比亚迪H股，减持的均价为217.67港元。
        
        这两次减持是巴菲特对比亚迪股份的主要减持行动，显示了他在持有比亚迪14年后开始逐步减少持股的策略。尽管巴菲特的减持行为引起市场关注，但似乎并未对比亚迪的股价产生长期负面影响。
        """

        output2 = """
        巴菲特减持比亚迪的市场环境可以从以下几个方面进行详细分析：
        
        1. 全球新能源汽车市场的增长：在巴菲特减持比亚迪的背景下，全球新能源汽车市场持续增长。新能源汽车因其环保特性在全球范围内受到推崇，尤其是在中国，政府对新能源汽车的支持政策不断，市场需求强劲。
        
        2. 中国数字经济的发展：2022年，中国数字经济规模达到50.2万亿元，占国内生产总值的比重提升至41.5%。数字经济的快速发展为新能源汽车行业，包括比亚迪在内的企业提供了强大的技术支持和市场环境。
        
        3. 比亚迪的股价和市场表现：尽管巴菲特的减持行为引发了市场的关注和短期波动，比亚迪的股价在7月12日确实出现了下跌，但从长期来看，
        比亚迪的股价并未因此受到严重影响。事实上，巴菲特此次减持的均价是近7次披露中的最高价格，显示出其对比亚迪长期价值的认可。
        
        4. 巴菲特减持的原因及其影响：巴菲特减持比亚迪的主要原因是为了更好的资金配置，而非对比亚迪前景的不看好。
        伯克希尔首席执行官沃伦·巴菲特明确表示，比亚迪是一家“卓越的公司”，并且在减持后，巴菲特依然保留了近10%的仓位在比亚迪。
        
        综上所述，巴菲特减持比亚迪的市场环境是在全球新能源汽车市场的持续增长、中国数字经济的快速发展背景下进行的。
        尽管市场对此有短暂的反应，但从长远看，比亚迪的市场表现和公司前景依然被看好。巴菲特的减持更多是基于资金配置的考虑，而非对比亚迪业务的负面评价。
        """

        output3 = """
        沃伦·巴菲特的投资策略以价值投资为核心，这种策略强调寻找那些价格低于其内在价值的股票，并持有这些股票直到市场价格反映出其真实价值。巴菲特在选择投资标的时，会重点考虑公司的财务健康状况、长期增长潜力、管理层质量以及市场定位等因素。他倾向于投资那些具有清晰业务模式和持续盈利能力的公司。
        
        关于巴菲特减持比亚迪的股份，这一行为可能受到多种因素的影响，其中包括但不限于比亚迪的市场估值、公司的业务发展以及整体市场环境的变化。巴菲特始终强调投资决策应基于公司的基本面分析，而非市场短期波动。因此，如果他认为比亚迪的市场估值超过了其内在价值，或者相比其他投资机会，比亚迪的吸引力减弱，这可能促使他减持持股。
        
        综合来看，巴菲特的价值投资策略和对投资标的持续评估是影响其决定是否减持比亚迪股份的重要因素。
        """

        output4 = """
        巴菲特减持比亚迪的行为对比亚迪有以下几方面的影响：
        
        1. 股价变动：巴菲特的减持行为可能短期内对比亚迪的股价造成压力。由于巴菲特被视为价值投资的典范，他的投资决策往往被市场解读为对被投资公司价值的一种评估。
        因此，他减持比亚迪的行为可能被市场解读为对比亚迪未来增长潜力的质疑，从而引发股价短期内的下跌。然而，具体的股价走势还需要结合公司的基本面和市场整体状况来综合判断。
        
        2. 投资者信心：巴菲特的减持可能会影响到部分投资者对比亚迪的信心。尤其是那些高度依赖于知名投资者行为的跟风投资者，他们可能会因为担心比亚迪的长期增长潜力而选择跟随减持。
        然而，对于那些更加关注公司基本面的投资者而言，只要比亚迪能够持续展现出良好的业绩和增长前景，他们的信心可能不会因此受到太大影响。
        
        综上所述，巴菲特减持比亚迪的行为对比亚迪股价和投资者信心都有一定影响，具体影响的程度和持续时间还需要根据市场的反应和比亚迪的业绩表现来进一步观察。
        """

        # mock the executing agent results
        executing_list = [{'input': '巴菲特减持比亚迪的具体情况是什么？包括减持的时间和数量。',  'output': output1},
                          {'input': '巴菲特减持比亚迪前后的市场环境是怎么样的？', 'output': output2},
                          {'input': '巴菲特的投资策略是什么？是否可能影响其决定减持比亚迪？', 'output': output3},
                          {'input': '巴菲特减持比亚迪对比亚迪的影响有哪些？比如可能的股价变动、投资者信心等。', 'output': output4}]
        executing_result = InputObject({'executing_result': executing_list})
        output_object: OutputObject = instance.run(input='分析下巴菲特减持比亚迪的原因',
                                                   executing_result=executing_result)
        res_info = f"\nExpressing agent execution result is :\n"
        res_info += f"{output_object.get_data('output')}"
        print(res_info)


if __name__ == '__main__':
    unittest.main()
