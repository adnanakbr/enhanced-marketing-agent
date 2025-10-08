# Copyright 2025 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Marketing_coordinator Agent assists in creating effective online content."""

from google.adk.agents import LlmAgent
from google.adk.tools.agent_tool import AgentTool

from . import prompt
from .sub_agents.banner_create import banner_create_agent
from .sub_agents.domain_create import domain_create_agent
from .sub_agents.logo_create import logo_create_agent
from .sub_agents.marketing_brief_create import marketing_brief_create_agent
from .sub_agents.marketing_create import marketing_create_agent
from .sub_agents.social_media_create import social_media_create_agent
from .sub_agents.visualization_create import visualization_create_agent
from .sub_agents.web_content_create import web_content_create_agent
from .sub_agents.website_create import website_create_agent

MODEL = "gemini-2.5-pro" 

marketing_coordinator = LlmAgent(
    name="marketing_coordinator",
    model=MODEL,
    description=(
        "Comprehensive marketing agency that helps you establish a powerful online presence "
        "and connect with your audience effectively. Based on your brand information, I can "
        "create visualizations, social media content, web content, marketing briefs, banners, "
        "and guide you through domain selection, website creation, marketing strategies, and logo design."
    ),
    instruction=prompt.MARKETING_COORDINATOR_PROMPT,
    tools=[
        AgentTool(agent=visualization_create_agent),
        AgentTool(agent=social_media_create_agent),
        AgentTool(agent=web_content_create_agent),
        AgentTool(agent=marketing_brief_create_agent),
        AgentTool(agent=banner_create_agent),
        AgentTool(agent=domain_create_agent),
        AgentTool(agent=website_create_agent),
        AgentTool(agent=marketing_create_agent),
        AgentTool(agent=logo_create_agent),
    ],
)

root_agent = marketing_coordinator
