# Repository Architecture

## Dependency Graph

```mermaid
graph TD;
    deploy_py["deploy.py"]
    click deploy_py "https://github.com/camel-ai/oasis/blob/main/deploy.py" "View source"
    subprocess(("subprocess"))
    deploy_py --> subprocess
    threading(("threading"))
    deploy_py --> threading
    time(("time"))
    deploy_py --> time
    requests(("requests"))
    deploy_py --> requests
    test_conftest_py["test/conftest.py"]
    click test_conftest_py "https://github.com/camel-ai/oasis/blob/main/test/conftest.py" "View source"
    os(("os"))
    test_conftest_py --> os
    sys(("sys"))
    test_conftest_py --> sys
    examples_custom_platform_simulation_py["examples/custom_platform_simulation.py"]
    click examples_custom_platform_simulation_py "https://github.com/camel-ai/oasis/blob/main/examples/custom_platform_simulation.py" "View source"
    asyncio(("asyncio"))
    examples_custom_platform_simulation_py --> asyncio
    os(("os"))
    examples_custom_platform_simulation_py --> os
    camel_models(("camel.models"))
    examples_custom_platform_simulation_py --> camel_models
    camel_types(("camel.types"))
    examples_custom_platform_simulation_py --> camel_types
    oasis(("oasis"))
    examples_custom_platform_simulation_py --> oasis
    oasis(("oasis"))
    examples_custom_platform_simulation_py --> oasis
    oasis_social_platform_channel(("oasis.social_platform.channel"))
    examples_custom_platform_simulation_py --> oasis_social_platform_channel
    oasis_social_platform_typing(("oasis.social_platform.typing"))
    examples_custom_platform_simulation_py --> oasis_social_platform_typing
    examples_twitter_simulation_vllm_py["examples/twitter_simulation_vllm.py"]
    click examples_twitter_simulation_vllm_py "https://github.com/camel-ai/oasis/blob/main/examples/twitter_simulation_vllm.py" "View source"
    asyncio(("asyncio"))
    examples_twitter_simulation_vllm_py --> asyncio
    os(("os"))
    examples_twitter_simulation_vllm_py --> os
    camel_models(("camel.models"))
    examples_twitter_simulation_vllm_py --> camel_models
    camel_types(("camel.types"))
    examples_twitter_simulation_vllm_py --> camel_types
    oasis(("oasis"))
    examples_twitter_simulation_vllm_py --> oasis
    oasis(("oasis"))
    examples_twitter_simulation_vllm_py --> oasis
    examples_twitter_simulation_openai_py["examples/twitter_simulation_openai.py"]
    click examples_twitter_simulation_openai_py "https://github.com/camel-ai/oasis/blob/main/examples/twitter_simulation_openai.py" "View source"
    asyncio(("asyncio"))
    examples_twitter_simulation_openai_py --> asyncio
    os(("os"))
    examples_twitter_simulation_openai_py --> os
    camel_models(("camel.models"))
    examples_twitter_simulation_openai_py --> camel_models
    camel_types(("camel.types"))
    examples_twitter_simulation_openai_py --> camel_types
    oasis(("oasis"))
    examples_twitter_simulation_openai_py --> oasis
    oasis(("oasis"))
    examples_twitter_simulation_openai_py --> oasis
    examples_custom_prompt_simulation_py["examples/custom_prompt_simulation.py"]
    click examples_custom_prompt_simulation_py "https://github.com/camel-ai/oasis/blob/main/examples/custom_prompt_simulation.py" "View source"
    asyncio(("asyncio"))
    examples_custom_prompt_simulation_py --> asyncio
    os(("os"))
    examples_custom_prompt_simulation_py --> os
    camel_models(("camel.models"))
    examples_custom_prompt_simulation_py --> camel_models
    camel_prompts(("camel.prompts"))
    examples_custom_prompt_simulation_py --> camel_prompts
    camel_types(("camel.types"))
    examples_custom_prompt_simulation_py --> camel_types
    oasis(("oasis"))
    examples_custom_prompt_simulation_py --> oasis
    oasis(("oasis"))
    examples_custom_prompt_simulation_py --> oasis
    examples_group_chat_simulation_py["examples/group_chat_simulation.py"]
    click examples_group_chat_simulation_py "https://github.com/camel-ai/oasis/blob/main/examples/group_chat_simulation.py" "View source"
    asyncio(("asyncio"))
    examples_group_chat_simulation_py --> asyncio
    os(("os"))
    examples_group_chat_simulation_py --> os
    camel_models(("camel.models"))
    examples_group_chat_simulation_py --> camel_models
    camel_types(("camel.types"))
    examples_group_chat_simulation_py --> camel_types
    oasis(("oasis"))
    examples_group_chat_simulation_py --> oasis
    oasis(("oasis"))
    examples_group_chat_simulation_py --> oasis
    examples_group_chat_simulation_oai_py["examples/group_chat_simulation_oai.py"]
    click examples_group_chat_simulation_oai_py "https://github.com/camel-ai/oasis/blob/main/examples/group_chat_simulation_oai.py" "View source"
    asyncio(("asyncio"))
    examples_group_chat_simulation_oai_py --> asyncio
    os(("os"))
    examples_group_chat_simulation_oai_py --> os
    camel_models(("camel.models"))
    examples_group_chat_simulation_oai_py --> camel_models
    camel_types(("camel.types"))
    examples_group_chat_simulation_oai_py --> camel_types
    oasis(("oasis"))
    examples_group_chat_simulation_oai_py --> oasis
    oasis(("oasis"))
    examples_group_chat_simulation_oai_py --> oasis
    examples_reddit_simulation_openai_py["examples/reddit_simulation_openai.py"]
    click examples_reddit_simulation_openai_py "https://github.com/camel-ai/oasis/blob/main/examples/reddit_simulation_openai.py" "View source"
    asyncio(("asyncio"))
    examples_reddit_simulation_openai_py --> asyncio
    os(("os"))
    examples_reddit_simulation_openai_py --> os
    camel_models(("camel.models"))
    examples_reddit_simulation_openai_py --> camel_models
    camel_types(("camel.types"))
    examples_reddit_simulation_openai_py --> camel_types
    oasis(("oasis"))
    examples_reddit_simulation_openai_py --> oasis
    oasis(("oasis"))
    examples_reddit_simulation_openai_py --> oasis
    examples___init___py["examples/__init__.py"]
    click examples___init___py "https://github.com/camel-ai/oasis/blob/main/examples/__init__.py" "View source"
    examples_search_tools_simulation_py["examples/search_tools_simulation.py"]
    click examples_search_tools_simulation_py "https://github.com/camel-ai/oasis/blob/main/examples/search_tools_simulation.py" "View source"
    asyncio(("asyncio"))
    examples_search_tools_simulation_py --> asyncio
    os(("os"))
    examples_search_tools_simulation_py --> os
    camel_models(("camel.models"))
    examples_search_tools_simulation_py --> camel_models
    camel_toolkits(("camel.toolkits"))
    examples_search_tools_simulation_py --> camel_toolkits
    camel_types(("camel.types"))
    examples_search_tools_simulation_py --> camel_types
    oasis(("oasis"))
    examples_search_tools_simulation_py --> oasis
    oasis(("oasis"))
    examples_search_tools_simulation_py --> oasis
    examples_sympy_tools_simulation_py["examples/sympy_tools_simulation.py"]
    click examples_sympy_tools_simulation_py "https://github.com/camel-ai/oasis/blob/main/examples/sympy_tools_simulation.py" "View source"
    asyncio(("asyncio"))
    examples_sympy_tools_simulation_py --> asyncio
    os(("os"))
    examples_sympy_tools_simulation_py --> os
    camel_models(("camel.models"))
    examples_sympy_tools_simulation_py --> camel_models
    camel_toolkits(("camel.toolkits"))
    examples_sympy_tools_simulation_py --> camel_toolkits
    camel_types(("camel.types"))
    examples_sympy_tools_simulation_py --> camel_types
    oasis(("oasis"))
    examples_sympy_tools_simulation_py --> oasis
    oasis(("oasis"))
    examples_sympy_tools_simulation_py --> oasis
    examples_twitter_interview_py["examples/twitter_interview.py"]
    click examples_twitter_interview_py "https://github.com/camel-ai/oasis/blob/main/examples/twitter_interview.py" "View source"
    asyncio(("asyncio"))
    examples_twitter_interview_py --> asyncio
    json(("json"))
    examples_twitter_interview_py --> json
    os(("os"))
    examples_twitter_interview_py --> os
    sqlite3(("sqlite3"))
    examples_twitter_interview_py --> sqlite3
    camel_models(("camel.models"))
    examples_twitter_interview_py --> camel_models
    camel_types(("camel.types"))
    examples_twitter_interview_py --> camel_types
    oasis(("oasis"))
    examples_twitter_interview_py --> oasis
    oasis(("oasis"))
    examples_twitter_interview_py --> oasis
    examples_twitter_misinforeport_py["examples/twitter_misinforeport.py"]
    click examples_twitter_misinforeport_py "https://github.com/camel-ai/oasis/blob/main/examples/twitter_misinforeport.py" "View source"
    asyncio(("asyncio"))
    examples_twitter_misinforeport_py --> asyncio
    json(("json"))
    examples_twitter_misinforeport_py --> json
    os(("os"))
    examples_twitter_misinforeport_py --> os
    sqlite3(("sqlite3"))
    examples_twitter_misinforeport_py --> sqlite3
    camel_models(("camel.models"))
    examples_twitter_misinforeport_py --> camel_models
    camel_types(("camel.types"))
    examples_twitter_misinforeport_py --> camel_types
    oasis(("oasis"))
    examples_twitter_misinforeport_py --> oasis
    oasis(("oasis"))
    examples_twitter_misinforeport_py --> oasis
    examples_quick_start_py["examples/quick_start.py"]
    click examples_quick_start_py "https://github.com/camel-ai/oasis/blob/main/examples/quick_start.py" "View source"
    asyncio(("asyncio"))
    examples_quick_start_py --> asyncio
    os(("os"))
    examples_quick_start_py --> os
    camel_models(("camel.models"))
    examples_quick_start_py --> camel_models
    camel_types(("camel.types"))
    examples_quick_start_py --> camel_types
    oasis(("oasis"))
    examples_quick_start_py --> oasis
    oasis(("oasis"))
    examples_quick_start_py --> oasis
    examples_different_model_simulation_py["examples/different_model_simulation.py"]
    click examples_different_model_simulation_py "https://github.com/camel-ai/oasis/blob/main/examples/different_model_simulation.py" "View source"
    asyncio(("asyncio"))
    examples_different_model_simulation_py --> asyncio
    os(("os"))
    examples_different_model_simulation_py --> os
    camel_models(("camel.models"))
    examples_different_model_simulation_py --> camel_models
    camel_types(("camel.types"))
    examples_different_model_simulation_py --> camel_types
    oasis(("oasis"))
    examples_different_model_simulation_py --> oasis
    oasis(("oasis"))
    examples_different_model_simulation_py --> oasis
    oasis___init___py["oasis/__init__.py"]
    click oasis___init___py "https://github.com/camel-ai/oasis/blob/main/oasis/__init__.py" "View source"
    oasis_environment_env_action(("oasis.environment.env_action"))
    oasis___init___py --> oasis_environment_env_action
    oasis_environment_make(("oasis.environment.make"))
    oasis___init___py --> oasis_environment_make
    oasis_social_agent(("oasis.social_agent"))
    oasis___init___py --> oasis_social_agent
    oasis_social_agent_agent(("oasis.social_agent.agent"))
    oasis___init___py --> oasis_social_agent_agent
    oasis_social_agent_agent_graph(("oasis.social_agent.agent_graph"))
    oasis___init___py --> oasis_social_agent_agent_graph
    oasis_social_platform_config(("oasis.social_platform.config"))
    oasis___init___py --> oasis_social_platform_config
    oasis_social_platform_platform(("oasis.social_platform.platform"))
    oasis___init___py --> oasis_social_platform_platform
    oasis_social_platform_typing(("oasis.social_platform.typing"))
    oasis___init___py --> oasis_social_platform_typing
    oasis_testing_show_db(("oasis.testing.show_db"))
    oasis___init___py --> oasis_testing_show_db
    licenses_update_license_py["licenses/update_license.py"]
    click licenses_update_license_py "https://github.com/camel-ai/oasis/blob/main/licenses/update_license.py" "View source"
    os(("os"))
    licenses_update_license_py --> os
    re(("re"))
    licenses_update_license_py --> re
    sys(("sys"))
    licenses_update_license_py --> sys
    pathlib(("pathlib"))
    licenses_update_license_py --> pathlib
    typing(("typing"))
    licenses_update_license_py --> typing
    test_agent_test_agent_custom_prompt_py["test/agent/test_agent_custom_prompt.py"]
    click test_agent_test_agent_custom_prompt_py "https://github.com/camel-ai/oasis/blob/main/test/agent/test_agent_custom_prompt.py" "View source"
    asyncio(("asyncio"))
    test_agent_test_agent_custom_prompt_py --> asyncio
    os(("os"))
    test_agent_test_agent_custom_prompt_py --> os
    os_path(("os.path"))
    test_agent_test_agent_custom_prompt_py --> os_path
    warnings(("warnings"))
    test_agent_test_agent_custom_prompt_py --> warnings
    pytest(("pytest"))
    test_agent_test_agent_custom_prompt_py --> pytest
    camel_prompts(("camel.prompts"))
    test_agent_test_agent_custom_prompt_py --> camel_prompts
    oasis_social_agent_agent(("oasis.social_agent.agent"))
    test_agent_test_agent_custom_prompt_py --> oasis_social_agent_agent
    oasis_social_platform_channel(("oasis.social_platform.channel"))
    test_agent_test_agent_custom_prompt_py --> oasis_social_platform_channel
    oasis_social_platform_config(("oasis.social_platform.config"))
    test_agent_test_agent_custom_prompt_py --> oasis_social_platform_config
    oasis_social_platform_platform(("oasis.social_platform.platform"))
    test_agent_test_agent_custom_prompt_py --> oasis_social_platform_platform
    test_agent_test_agent_graph_py["test/agent/test_agent_graph.py"]
    click test_agent_test_agent_graph_py "https://github.com/camel-ai/oasis/blob/main/test/agent/test_agent_graph.py" "View source"
    os(("os"))
    test_agent_test_agent_graph_py --> os
    os_path(("os.path"))
    test_agent_test_agent_graph_py --> os_path
    pytest(("pytest"))
    test_agent_test_agent_graph_py --> pytest
    oasis_social_agent_agent(("oasis.social_agent.agent"))
    test_agent_test_agent_graph_py --> oasis_social_agent_agent
    oasis_social_agent_agent_graph(("oasis.social_agent.agent_graph"))
    test_agent_test_agent_graph_py --> oasis_social_agent_agent_graph
    oasis_social_platform_channel(("oasis.social_platform.channel"))
    test_agent_test_agent_graph_py --> oasis_social_platform_channel
    oasis_social_platform_config(("oasis.social_platform.config"))
    test_agent_test_agent_graph_py --> oasis_social_platform_config
    test_agent_test_multi_agent_signup_create_py["test/agent/test_multi_agent_signup_create.py"]
    click test_agent_test_multi_agent_signup_create_py "https://github.com/camel-ai/oasis/blob/main/test/agent/test_multi_agent_signup_create.py" "View source"
    asyncio(("asyncio"))
    test_agent_test_multi_agent_signup_create_py --> asyncio
    os(("os"))
    test_agent_test_multi_agent_signup_create_py --> os
    os_path(("os.path"))
    test_agent_test_multi_agent_signup_create_py --> os_path
    random(("random"))
    test_agent_test_multi_agent_signup_create_py --> random
    sqlite3(("sqlite3"))
    test_agent_test_multi_agent_signup_create_py --> sqlite3
    pytest(("pytest"))
    test_agent_test_multi_agent_signup_create_py --> pytest
    oasis_social_agent_agent(("oasis.social_agent.agent"))
    test_agent_test_multi_agent_signup_create_py --> oasis_social_agent_agent
    oasis_social_platform_channel(("oasis.social_platform.channel"))
    test_agent_test_multi_agent_signup_create_py --> oasis_social_platform_channel
    oasis_social_platform_config(("oasis.social_platform.config"))
    test_agent_test_multi_agent_signup_create_py --> oasis_social_platform_config
    oasis_social_platform_platform(("oasis.social_platform.platform"))
    test_agent_test_multi_agent_signup_create_py --> oasis_social_platform_platform
    oasis_testing_show_db(("oasis.testing.show_db"))
    test_agent_test_multi_agent_signup_create_py --> oasis_testing_show_db
    test_agent_test_agent_tools_py["test/agent/test_agent_tools.py"]
    click test_agent_test_agent_tools_py "https://github.com/camel-ai/oasis/blob/main/test/agent/test_agent_tools.py" "View source"
    asyncio(("asyncio"))
    test_agent_test_agent_tools_py --> asyncio
    os(("os"))
    test_agent_test_agent_tools_py --> os
    os_path(("os.path"))
    test_agent_test_agent_tools_py --> os_path
    pytest(("pytest"))
    test_agent_test_agent_tools_py --> pytest
    camel_toolkits(("camel.toolkits"))
    test_agent_test_agent_tools_py --> camel_toolkits
    oasis(("oasis"))
    test_agent_test_agent_tools_py --> oasis
    oasis_social_agent_agent(("oasis.social_agent.agent"))
    test_agent_test_agent_tools_py --> oasis_social_agent_agent
    oasis_social_platform_channel(("oasis.social_platform.channel"))
    test_agent_test_agent_tools_py --> oasis_social_platform_channel
    oasis_social_platform_config(("oasis.social_platform.config"))
    test_agent_test_agent_tools_py --> oasis_social_platform_config
    oasis_social_platform_platform(("oasis.social_platform.platform"))
    test_agent_test_agent_tools_py --> oasis_social_platform_platform
    test_agent_test_interview_action_py["test/agent/test_interview_action.py"]
    click test_agent_test_interview_action_py "https://github.com/camel-ai/oasis/blob/main/test/agent/test_interview_action.py" "View source"
    asyncio(("asyncio"))
    test_agent_test_interview_action_py --> asyncio
    json(("json"))
    test_agent_test_interview_action_py --> json
    os(("os"))
    test_agent_test_interview_action_py --> os
    os_path(("os.path"))
    test_agent_test_interview_action_py --> os_path
    sqlite3(("sqlite3"))
    test_agent_test_interview_action_py --> sqlite3
    tempfile(("tempfile"))
    test_agent_test_interview_action_py --> tempfile
    pytest(("pytest"))
    test_agent_test_interview_action_py --> pytest
    camel_models(("camel.models"))
    test_agent_test_interview_action_py --> camel_models
    camel_types(("camel.types"))
    test_agent_test_interview_action_py --> camel_types
    oasis(("oasis"))
    test_agent_test_interview_action_py --> oasis
    oasis(("oasis"))
    test_agent_test_interview_action_py --> oasis
    oasis_social_agent_agent(("oasis.social_agent.agent"))
    test_agent_test_interview_action_py --> oasis_social_agent_agent
    oasis_social_platform_channel(("oasis.social_platform.channel"))
    test_agent_test_interview_action_py --> oasis_social_platform_channel
    oasis_social_platform_config(("oasis.social_platform.config"))
    test_agent_test_interview_action_py --> oasis_social_platform_config
    oasis_social_platform_platform(("oasis.social_platform.platform"))
    test_agent_test_interview_action_py --> oasis_social_platform_platform
    test_agent_test_twitter_user_agent_all_actions_py["test/agent/test_twitter_user_agent_all_actions.py"]
    click test_agent_test_twitter_user_agent_all_actions_py "https://github.com/camel-ai/oasis/blob/main/test/agent/test_twitter_user_agent_all_actions.py" "View source"
    asyncio(("asyncio"))
    test_agent_test_twitter_user_agent_all_actions_py --> asyncio
    os(("os"))
    test_agent_test_twitter_user_agent_all_actions_py --> os
    os_path(("os.path"))
    test_agent_test_twitter_user_agent_all_actions_py --> os_path
    random(("random"))
    test_agent_test_twitter_user_agent_all_actions_py --> random
    pytest(("pytest"))
    test_agent_test_twitter_user_agent_all_actions_py --> pytest
    oasis_social_agent_agent(("oasis.social_agent.agent"))
    test_agent_test_twitter_user_agent_all_actions_py --> oasis_social_agent_agent
    oasis_social_platform_channel(("oasis.social_platform.channel"))
    test_agent_test_twitter_user_agent_all_actions_py --> oasis_social_platform_channel
    oasis_social_platform_config(("oasis.social_platform.config"))
    test_agent_test_twitter_user_agent_all_actions_py --> oasis_social_platform_config
    oasis_social_platform_platform(("oasis.social_platform.platform"))
    test_agent_test_twitter_user_agent_all_actions_py --> oasis_social_platform_platform
    oasis_social_platform_typing(("oasis.social_platform.typing"))
    test_agent_test_twitter_user_agent_all_actions_py --> oasis_social_platform_typing
    test_agent_test_agent_generator_py["test/agent/test_agent_generator.py"]
    click test_agent_test_agent_generator_py "https://github.com/camel-ai/oasis/blob/main/test/agent/test_agent_generator.py" "View source"
    asyncio(("asyncio"))
    test_agent_test_agent_generator_py --> asyncio
    os(("os"))
    test_agent_test_agent_generator_py --> os
    os_path(("os.path"))
    test_agent_test_agent_generator_py --> os_path
    pytest(("pytest"))
    test_agent_test_agent_generator_py --> pytest
    camel_models(("camel.models"))
    test_agent_test_agent_generator_py --> camel_models
    camel_types(("camel.types"))
    test_agent_test_agent_generator_py --> camel_types
    oasis_social_agent_agents_generator(("oasis.social_agent.agents_generator"))
    test_agent_test_agent_generator_py --> oasis_social_agent_agents_generator
    oasis_social_platform_channel(("oasis.social_platform.channel"))
    test_agent_test_agent_generator_py --> oasis_social_platform_channel
    oasis_social_platform_platform(("oasis.social_platform.platform"))
    test_agent_test_agent_generator_py --> oasis_social_platform_platform
    test_agent_test_action_docstring_py["test/agent/test_action_docstring.py"]
    click test_agent_test_action_docstring_py "https://github.com/camel-ai/oasis/blob/main/test/agent/test_action_docstring.py" "View source"
    typing(("typing"))
    test_agent_test_action_docstring_py --> typing
    camel_toolkits(("camel.toolkits"))
    test_agent_test_action_docstring_py --> camel_toolkits
    oasis_social_agent_agent(("oasis.social_agent.agent"))
    test_agent_test_action_docstring_py --> oasis_social_agent_agent
    test_infra_database_test_post_self_rating_py["test/infra/database/test_post_self_rating.py"]
    click test_infra_database_test_post_self_rating_py "https://github.com/camel-ai/oasis/blob/main/test/infra/database/test_post_self_rating.py" "View source"
    os(("os"))
    test_infra_database_test_post_self_rating_py --> os
    os_path(("os.path"))
    test_infra_database_test_post_self_rating_py --> os_path
    sqlite3(("sqlite3"))
    test_infra_database_test_post_self_rating_py --> sqlite3
    pytest(("pytest"))
    test_infra_database_test_post_self_rating_py --> pytest
    oasis_social_platform_platform(("oasis.social_platform.platform"))
    test_infra_database_test_post_self_rating_py --> oasis_social_platform_platform
    test_infra_database_test_comment_self_rating_py["test/infra/database/test_comment_self_rating.py"]
    click test_infra_database_test_comment_self_rating_py "https://github.com/camel-ai/oasis/blob/main/test/infra/database/test_comment_self_rating.py" "View source"
    os(("os"))
    test_infra_database_test_comment_self_rating_py --> os
    os_path(("os.path"))
    test_infra_database_test_comment_self_rating_py --> os_path
    sqlite3(("sqlite3"))
    test_infra_database_test_comment_self_rating_py --> sqlite3
    pytest(("pytest"))
    test_infra_database_test_comment_self_rating_py --> pytest
    oasis_social_platform_platform(("oasis.social_platform.platform"))
    test_infra_database_test_comment_self_rating_py --> oasis_social_platform_platform
    test_infra_database_test_search_py["test/infra/database/test_search.py"]
    click test_infra_database_test_search_py "https://github.com/camel-ai/oasis/blob/main/test/infra/database/test_search.py" "View source"
    os(("os"))
    test_infra_database_test_search_py --> os
    os_path(("os.path"))
    test_infra_database_test_search_py --> os_path
    sqlite3(("sqlite3"))
    test_infra_database_test_search_py --> sqlite3
    pytest(("pytest"))
    test_infra_database_test_search_py --> pytest
    oasis_social_platform_platform(("oasis.social_platform.platform"))
    test_infra_database_test_search_py --> oasis_social_platform_platform
    test_infra_database_test_user_py["test/infra/database/test_user.py"]
    click test_infra_database_test_user_py "https://github.com/camel-ai/oasis/blob/main/test/infra/database/test_user.py" "View source"
    os(("os"))
    test_infra_database_test_user_py --> os
    os_path(("os.path"))
    test_infra_database_test_user_py --> os_path
    sqlite3(("sqlite3"))
    test_infra_database_test_user_py --> sqlite3
    pytest(("pytest"))
    test_infra_database_test_user_py --> pytest
    oasis_social_platform_platform(("oasis.social_platform.platform"))
    test_infra_database_test_user_py --> oasis_social_platform_platform
    test_infra_database_test_group_chat_py["test/infra/database/test_group_chat.py"]
    click test_infra_database_test_group_chat_py "https://github.com/camel-ai/oasis/blob/main/test/infra/database/test_group_chat.py" "View source"
    os(("os"))
    test_infra_database_test_group_chat_py --> os
    os_path(("os.path"))
    test_infra_database_test_group_chat_py --> os_path
    sqlite3(("sqlite3"))
    test_infra_database_test_group_chat_py --> sqlite3
    pytest(("pytest"))
    test_infra_database_test_group_chat_py --> pytest
    oasis_social_platform_platform(("oasis.social_platform.platform"))
    test_infra_database_test_group_chat_py --> oasis_social_platform_platform
    test_infra_database_test_refresh_score_py["test/infra/database/test_refresh_score.py"]
    click test_infra_database_test_refresh_score_py "https://github.com/camel-ai/oasis/blob/main/test/infra/database/test_refresh_score.py" "View source"
    os(("os"))
    test_infra_database_test_refresh_score_py --> os
    os_path(("os.path"))
    test_infra_database_test_refresh_score_py --> os_path
    sqlite3(("sqlite3"))
    test_infra_database_test_refresh_score_py --> sqlite3
    datetime(("datetime"))
    test_infra_database_test_refresh_score_py --> datetime
    pytest(("pytest"))
    test_infra_database_test_refresh_score_py --> pytest
    oasis_social_platform_platform(("oasis.social_platform.platform"))
    test_infra_database_test_refresh_score_py --> oasis_social_platform_platform
    oasis_social_platform_typing(("oasis.social_platform.typing"))
    test_infra_database_test_refresh_score_py --> oasis_social_platform_typing
    test_infra_database_test_multi_create_post_py["test/infra/database/test_multi_create_post.py"]
    click test_infra_database_test_multi_create_post_py "https://github.com/camel-ai/oasis/blob/main/test/infra/database/test_multi_create_post.py" "View source"
    os(("os"))
    test_infra_database_test_multi_create_post_py --> os
    os_path(("os.path"))
    test_infra_database_test_multi_create_post_py --> os_path
    sqlite3(("sqlite3"))
    test_infra_database_test_multi_create_post_py --> sqlite3
    pytest(("pytest"))
    test_infra_database_test_multi_create_post_py --> pytest
    oasis_social_platform_platform(("oasis.social_platform.platform"))
    test_infra_database_test_multi_create_post_py --> oasis_social_platform_platform
    oasis_testing_show_db(("oasis.testing.show_db"))
    test_infra_database_test_multi_create_post_py --> oasis_testing_show_db
    test_infra_database_test_product_py["test/infra/database/test_product.py"]
    click test_infra_database_test_product_py "https://github.com/camel-ai/oasis/blob/main/test/infra/database/test_product.py" "View source"
    os(("os"))
    test_infra_database_test_product_py --> os
    os_path(("os.path"))
    test_infra_database_test_product_py --> os_path
    sqlite3(("sqlite3"))
    test_infra_database_test_product_py --> sqlite3
    pytest(("pytest"))
    test_infra_database_test_product_py --> pytest
    oasis_social_platform_platform(("oasis.social_platform.platform"))
    test_infra_database_test_product_py --> oasis_social_platform_platform
    oasis_social_platform_typing(("oasis.social_platform.typing"))
    test_infra_database_test_product_py --> oasis_social_platform_typing
    test_infra_database_test_post_py["test/infra/database/test_post.py"]
    click test_infra_database_test_post_py "https://github.com/camel-ai/oasis/blob/main/test/infra/database/test_post.py" "View source"
    os(("os"))
    test_infra_database_test_post_py --> os
    os_path(("os.path"))
    test_infra_database_test_post_py --> os_path
    sqlite3(("sqlite3"))
    test_infra_database_test_post_py --> sqlite3
    pytest(("pytest"))
    test_infra_database_test_post_py --> pytest
    oasis_social_platform_platform(("oasis.social_platform.platform"))
    test_infra_database_test_post_py --> oasis_social_platform_platform
    test_infra_database_test_create_fetch_database_py["test/infra/database/test_create_fetch_database.py"]
    click test_infra_database_test_create_fetch_database_py "https://github.com/camel-ai/oasis/blob/main/test/infra/database/test_create_fetch_database.py" "View source"
    datetime(("datetime"))
    test_infra_database_test_create_fetch_database_py --> datetime
    os(("os"))
    test_infra_database_test_create_fetch_database_py --> os
    os_path(("os.path"))
    test_infra_database_test_create_fetch_database_py --> os_path
    sqlite3(("sqlite3"))
    test_infra_database_test_create_fetch_database_py --> sqlite3
    pytest(("pytest"))
    test_infra_database_test_create_fetch_database_py --> pytest
    oasis_social_platform_database(("oasis.social_platform.database"))
    test_infra_database_test_create_fetch_database_py --> oasis_social_platform_database
    test_infra_database_test_refresh_py["test/infra/database/test_refresh.py"]
    click test_infra_database_test_refresh_py "https://github.com/camel-ai/oasis/blob/main/test/infra/database/test_refresh.py" "View source"
    os(("os"))
    test_infra_database_test_refresh_py --> os
    os_path(("os.path"))
    test_infra_database_test_refresh_py --> os_path
    sqlite3(("sqlite3"))
    test_infra_database_test_refresh_py --> sqlite3
    datetime(("datetime"))
    test_infra_database_test_refresh_py --> datetime
    pytest(("pytest"))
    test_infra_database_test_refresh_py --> pytest
    oasis_social_platform_platform(("oasis.social_platform.platform"))
    test_infra_database_test_refresh_py --> oasis_social_platform_platform
    oasis_social_platform_typing(("oasis.social_platform.typing"))
    test_infra_database_test_refresh_py --> oasis_social_platform_typing
    test_infra_database_test_multi_user_signup_py["test/infra/database/test_multi_user_signup.py"]
    click test_infra_database_test_multi_user_signup_py "https://github.com/camel-ai/oasis/blob/main/test/infra/database/test_multi_user_signup.py" "View source"
    os(("os"))
    test_infra_database_test_multi_user_signup_py --> os
    os_path(("os.path"))
    test_infra_database_test_multi_user_signup_py --> os_path
    sqlite3(("sqlite3"))
    test_infra_database_test_multi_user_signup_py --> sqlite3
    datetime(("datetime"))
    test_infra_database_test_multi_user_signup_py --> datetime
    oasis_social_platform_database(("oasis.social_platform.database"))
    test_infra_database_test_multi_user_signup_py --> oasis_social_platform_database
    test_infra_database_test_trend_py["test/infra/database/test_trend.py"]
    click test_infra_database_test_trend_py "https://github.com/camel-ai/oasis/blob/main/test/infra/database/test_trend.py" "View source"
    os(("os"))
    test_infra_database_test_trend_py --> os
    os_path(("os.path"))
    test_infra_database_test_trend_py --> os_path
    sqlite3(("sqlite3"))
    test_infra_database_test_trend_py --> sqlite3
    datetime(("datetime"))
    test_infra_database_test_trend_py --> datetime
    pytest(("pytest"))
    test_infra_database_test_trend_py --> pytest
    oasis_social_platform_platform(("oasis.social_platform.platform"))
    test_infra_database_test_trend_py --> oasis_social_platform_platform
    test_infra_database_test_report_post_py["test/infra/database/test_report_post.py"]
    click test_infra_database_test_report_post_py "https://github.com/camel-ai/oasis/blob/main/test/infra/database/test_report_post.py" "View source"
    os(("os"))
    test_infra_database_test_report_post_py --> os
    os_path(("os.path"))
    test_infra_database_test_report_post_py --> os_path
    sqlite3(("sqlite3"))
    test_infra_database_test_report_post_py --> sqlite3
    pytest(("pytest"))
    test_infra_database_test_report_post_py --> pytest
    oasis_social_platform_platform(("oasis.social_platform.platform"))
    test_infra_database_test_report_post_py --> oasis_social_platform_platform
    test_infra_database_test_do_nothing_py["test/infra/database/test_do_nothing.py"]
    click test_infra_database_test_do_nothing_py "https://github.com/camel-ai/oasis/blob/main/test/infra/database/test_do_nothing.py" "View source"
    os(("os"))
    test_infra_database_test_do_nothing_py --> os
    os_path(("os.path"))
    test_infra_database_test_do_nothing_py --> os_path
    sqlite3(("sqlite3"))
    test_infra_database_test_do_nothing_py --> sqlite3
    pytest(("pytest"))
    test_infra_database_test_do_nothing_py --> pytest
    oasis_social_platform_platform(("oasis.social_platform.platform"))
    test_infra_database_test_do_nothing_py --> oasis_social_platform_platform
    oasis_social_platform_typing(("oasis.social_platform.typing"))
    test_infra_database_test_do_nothing_py --> oasis_social_platform_typing
    test_infra_database_test_user_create_post_py["test/infra/database/test_user_create_post.py"]
    click test_infra_database_test_user_create_post_py "https://github.com/camel-ai/oasis/blob/main/test/infra/database/test_user_create_post.py" "View source"
    os(("os"))
    test_infra_database_test_user_create_post_py --> os
    os_path(("os.path"))
    test_infra_database_test_user_create_post_py --> os_path
    sqlite3(("sqlite3"))
    test_infra_database_test_user_create_post_py --> sqlite3
    pytest(("pytest"))
    test_infra_database_test_user_create_post_py --> pytest
    oasis_social_platform_platform(("oasis.social_platform.platform"))
    test_infra_database_test_user_create_post_py --> oasis_social_platform_platform
    test_infra_database_test_user_signup_py["test/infra/database/test_user_signup.py"]
    click test_infra_database_test_user_signup_py "https://github.com/camel-ai/oasis/blob/main/test/infra/database/test_user_signup.py" "View source"
    os(("os"))
    test_infra_database_test_user_signup_py --> os
    os_path(("os.path"))
    test_infra_database_test_user_signup_py --> os_path
    sqlite3(("sqlite3"))
    test_infra_database_test_user_signup_py --> sqlite3
    pytest(("pytest"))
    test_infra_database_test_user_signup_py --> pytest
    oasis_social_platform_platform(("oasis.social_platform.platform"))
    test_infra_database_test_user_signup_py --> oasis_social_platform_platform
    test_infra_database_test_comment_py["test/infra/database/test_comment.py"]
    click test_infra_database_test_comment_py "https://github.com/camel-ai/oasis/blob/main/test/infra/database/test_comment.py" "View source"
    os(("os"))
    test_infra_database_test_comment_py --> os
    os_path(("os.path"))
    test_infra_database_test_comment_py --> os_path
    sqlite3(("sqlite3"))
    test_infra_database_test_comment_py --> sqlite3
    pytest(("pytest"))
    test_infra_database_test_comment_py --> pytest
    oasis_social_platform_platform(("oasis.social_platform.platform"))
    test_infra_database_test_comment_py --> oasis_social_platform_platform
    test_infra_database_test_quote_repost_refresh_py["test/infra/database/test_quote_repost_refresh.py"]
    click test_infra_database_test_quote_repost_refresh_py "https://github.com/camel-ai/oasis/blob/main/test/infra/database/test_quote_repost_refresh.py" "View source"
    os(("os"))
    test_infra_database_test_quote_repost_refresh_py --> os
    os_path(("os.path"))
    test_infra_database_test_quote_repost_refresh_py --> os_path
    sqlite3(("sqlite3"))
    test_infra_database_test_quote_repost_refresh_py --> sqlite3
    pytest(("pytest"))
    test_infra_database_test_quote_repost_refresh_py --> pytest
    oasis_social_platform_platform(("oasis.social_platform.platform"))
    test_infra_database_test_quote_repost_refresh_py --> oasis_social_platform_platform
    oasis_social_platform_typing(("oasis.social_platform.typing"))
    test_infra_database_test_quote_repost_refresh_py --> oasis_social_platform_typing
    test_infra_recsys_test_update_rec_table_py["test/infra/recsys/test_update_rec_table.py"]
    click test_infra_recsys_test_update_rec_table_py "https://github.com/camel-ai/oasis/blob/main/test/infra/recsys/test_update_rec_table.py" "View source"
    asyncio(("asyncio"))
    test_infra_recsys_test_update_rec_table_py --> asyncio
    os(("os"))
    test_infra_recsys_test_update_rec_table_py --> os
    os_path(("os.path"))
    test_infra_recsys_test_update_rec_table_py --> os_path
    random(("random"))
    test_infra_recsys_test_update_rec_table_py --> random
    sqlite3(("sqlite3"))
    test_infra_recsys_test_update_rec_table_py --> sqlite3
    pytest(("pytest"))
    test_infra_recsys_test_update_rec_table_py --> pytest
    oasis_social_platform_channel(("oasis.social_platform.channel"))
    test_infra_recsys_test_update_rec_table_py --> oasis_social_platform_channel
    oasis_social_platform_platform(("oasis.social_platform.platform"))
    test_infra_recsys_test_update_rec_table_py --> oasis_social_platform_platform
    oasis_social_platform_recsys(("oasis.social_platform.recsys"))
    test_infra_recsys_test_update_rec_table_py --> oasis_social_platform_recsys
    oasis_social_platform_typing(("oasis.social_platform.typing"))
    test_infra_recsys_test_update_rec_table_py --> oasis_social_platform_typing
    oasis_testing_show_db(("oasis.testing.show_db"))
    test_infra_recsys_test_update_rec_table_py --> oasis_testing_show_db
    test_infra_recsys_test_recsys_py["test/infra/recsys/test_recsys.py"]
    click test_infra_recsys_test_recsys_py "https://github.com/camel-ai/oasis/blob/main/test/infra/recsys/test_recsys.py" "View source"
    oasis_social_platform_recsys(("oasis.social_platform.recsys"))
    test_infra_recsys_test_recsys_py --> oasis_social_platform_recsys
    test_infra_recsys_test_update_rec_table_reddit_py["test/infra/recsys/test_update_rec_table_reddit.py"]
    click test_infra_recsys_test_update_rec_table_reddit_py "https://github.com/camel-ai/oasis/blob/main/test/infra/recsys/test_update_rec_table_reddit.py" "View source"
    asyncio(("asyncio"))
    test_infra_recsys_test_update_rec_table_reddit_py --> asyncio
    os(("os"))
    test_infra_recsys_test_update_rec_table_reddit_py --> os
    os_path(("os.path"))
    test_infra_recsys_test_update_rec_table_reddit_py --> os_path
    sqlite3(("sqlite3"))
    test_infra_recsys_test_update_rec_table_reddit_py --> sqlite3
    datetime(("datetime"))
    test_infra_recsys_test_update_rec_table_reddit_py --> datetime
    pytest(("pytest"))
    test_infra_recsys_test_update_rec_table_reddit_py --> pytest
    oasis_social_platform_channel(("oasis.social_platform.channel"))
    test_infra_recsys_test_update_rec_table_reddit_py --> oasis_social_platform_channel
    oasis_social_platform_platform(("oasis.social_platform.platform"))
    test_infra_recsys_test_update_rec_table_reddit_py --> oasis_social_platform_platform
    oasis_social_platform_typing(("oasis.social_platform.typing"))
    test_infra_recsys_test_update_rec_table_reddit_py --> oasis_social_platform_typing
    examples_experiment___init___py["examples/experiment/__init__.py"]
    click examples_experiment___init___py "https://github.com/camel-ai/oasis/blob/main/examples/experiment/__init__.py" "View source"
    examples_experiment_utils_py["examples/experiment/utils.py"]
    click examples_experiment_utils_py "https://github.com/camel-ai/oasis/blob/main/examples/experiment/utils.py" "View source"
    examples_experiment_twitter_gpt_example_openai_embedding_twitter_simulation_py["examples/experiment/twitter_gpt_example_openai_embedding/twitter_simulation.py"]
    click examples_experiment_twitter_gpt_example_openai_embedding_twitter_simulation_py "https://github.com/camel-ai/oasis/blob/main/examples/experiment/twitter_gpt_example_openai_embedding/twitter_simulation.py" "View source"
    __future__(("__future__"))
    examples_experiment_twitter_gpt_example_openai_embedding_twitter_simulation_py --> __future__
    argparse(("argparse"))
    examples_experiment_twitter_gpt_example_openai_embedding_twitter_simulation_py --> argparse
    asyncio(("asyncio"))
    examples_experiment_twitter_gpt_example_openai_embedding_twitter_simulation_py --> asyncio
    logging(("logging"))
    examples_experiment_twitter_gpt_example_openai_embedding_twitter_simulation_py --> logging
    os(("os"))
    examples_experiment_twitter_gpt_example_openai_embedding_twitter_simulation_py --> os
    random(("random"))
    examples_experiment_twitter_gpt_example_openai_embedding_twitter_simulation_py --> random
    sys(("sys"))
    examples_experiment_twitter_gpt_example_openai_embedding_twitter_simulation_py --> sys
    datetime(("datetime"))
    examples_experiment_twitter_gpt_example_openai_embedding_twitter_simulation_py --> datetime
    pathlib(("pathlib"))
    examples_experiment_twitter_gpt_example_openai_embedding_twitter_simulation_py --> pathlib
    typing(("typing"))
    examples_experiment_twitter_gpt_example_openai_embedding_twitter_simulation_py --> typing
    pandas(("pandas"))
    examples_experiment_twitter_gpt_example_openai_embedding_twitter_simulation_py --> pandas
    colorama(("colorama"))
    examples_experiment_twitter_gpt_example_openai_embedding_twitter_simulation_py --> colorama
    yaml(("yaml"))
    examples_experiment_twitter_gpt_example_openai_embedding_twitter_simulation_py --> yaml
    camel_models(("camel.models"))
    examples_experiment_twitter_gpt_example_openai_embedding_twitter_simulation_py --> camel_models
    camel_types(("camel.types"))
    examples_experiment_twitter_gpt_example_openai_embedding_twitter_simulation_py --> camel_types
    oasis_clock_clock(("oasis.clock.clock"))
    examples_experiment_twitter_gpt_example_openai_embedding_twitter_simulation_py --> oasis_clock_clock
    oasis_social_agent_agents_generator(("oasis.social_agent.agents_generator"))
    examples_experiment_twitter_gpt_example_openai_embedding_twitter_simulation_py --> oasis_social_agent_agents_generator
    oasis_social_platform_channel(("oasis.social_platform.channel"))
    examples_experiment_twitter_gpt_example_openai_embedding_twitter_simulation_py --> oasis_social_platform_channel
    oasis_social_platform_platform(("oasis.social_platform.platform"))
    examples_experiment_twitter_gpt_example_openai_embedding_twitter_simulation_py --> oasis_social_platform_platform
    oasis_social_platform_typing(("oasis.social_platform.typing"))
    examples_experiment_twitter_gpt_example_openai_embedding_twitter_simulation_py --> oasis_social_platform_typing
    examples_experiment_reddit_simulation_counterfactual_reddit_simulation_counterfactual_py["examples/experiment/reddit_simulation_counterfactual/reddit_simulation_counterfactual.py"]
    click examples_experiment_reddit_simulation_counterfactual_reddit_simulation_counterfactual_py "https://github.com/camel-ai/oasis/blob/main/examples/experiment/reddit_simulation_counterfactual/reddit_simulation_counterfactual.py" "View source"
    __future__(("__future__"))
    examples_experiment_reddit_simulation_counterfactual_reddit_simulation_counterfactual_py --> __future__
    argparse(("argparse"))
    examples_experiment_reddit_simulation_counterfactual_reddit_simulation_counterfactual_py --> argparse
    asyncio(("asyncio"))
    examples_experiment_reddit_simulation_counterfactual_reddit_simulation_counterfactual_py --> asyncio
    json(("json"))
    examples_experiment_reddit_simulation_counterfactual_reddit_simulation_counterfactual_py --> json
    logging(("logging"))
    examples_experiment_reddit_simulation_counterfactual_reddit_simulation_counterfactual_py --> logging
    os(("os"))
    examples_experiment_reddit_simulation_counterfactual_reddit_simulation_counterfactual_py --> os
    random(("random"))
    examples_experiment_reddit_simulation_counterfactual_reddit_simulation_counterfactual_py --> random
    sys(("sys"))
    examples_experiment_reddit_simulation_counterfactual_reddit_simulation_counterfactual_py --> sys
    datetime(("datetime"))
    examples_experiment_reddit_simulation_counterfactual_reddit_simulation_counterfactual_py --> datetime
    typing(("typing"))
    examples_experiment_reddit_simulation_counterfactual_reddit_simulation_counterfactual_py --> typing
    camel_models(("camel.models"))
    examples_experiment_reddit_simulation_counterfactual_reddit_simulation_counterfactual_py --> camel_models
    camel_types(("camel.types"))
    examples_experiment_reddit_simulation_counterfactual_reddit_simulation_counterfactual_py --> camel_types
    colorama(("colorama"))
    examples_experiment_reddit_simulation_counterfactual_reddit_simulation_counterfactual_py --> colorama
    yaml(("yaml"))
    examples_experiment_reddit_simulation_counterfactual_reddit_simulation_counterfactual_py --> yaml
    utils(("utils"))
    examples_experiment_reddit_simulation_counterfactual_reddit_simulation_counterfactual_py --> utils
    oasis_clock_clock(("oasis.clock.clock"))
    examples_experiment_reddit_simulation_counterfactual_reddit_simulation_counterfactual_py --> oasis_clock_clock
    oasis_social_agent_agents_generator(("oasis.social_agent.agents_generator"))
    examples_experiment_reddit_simulation_counterfactual_reddit_simulation_counterfactual_py --> oasis_social_agent_agents_generator
    oasis_social_platform_channel(("oasis.social_platform.channel"))
    examples_experiment_reddit_simulation_counterfactual_reddit_simulation_counterfactual_py --> oasis_social_platform_channel
    oasis_social_platform_platform(("oasis.social_platform.platform"))
    examples_experiment_reddit_simulation_counterfactual_reddit_simulation_counterfactual_py --> oasis_social_platform_platform
    oasis_social_platform_typing(("oasis.social_platform.typing"))
    examples_experiment_reddit_simulation_counterfactual_reddit_simulation_counterfactual_py --> oasis_social_platform_typing
    examples_experiment_twitter_gpt_example_twitter_simulation_py["examples/experiment/twitter_gpt_example/twitter_simulation.py"]
    click examples_experiment_twitter_gpt_example_twitter_simulation_py "https://github.com/camel-ai/oasis/blob/main/examples/experiment/twitter_gpt_example/twitter_simulation.py" "View source"
    __future__(("__future__"))
    examples_experiment_twitter_gpt_example_twitter_simulation_py --> __future__
    argparse(("argparse"))
    examples_experiment_twitter_gpt_example_twitter_simulation_py --> argparse
    asyncio(("asyncio"))
    examples_experiment_twitter_gpt_example_twitter_simulation_py --> asyncio
    logging(("logging"))
    examples_experiment_twitter_gpt_example_twitter_simulation_py --> logging
    os(("os"))
    examples_experiment_twitter_gpt_example_twitter_simulation_py --> os
    random(("random"))
    examples_experiment_twitter_gpt_example_twitter_simulation_py --> random
    sys(("sys"))
    examples_experiment_twitter_gpt_example_twitter_simulation_py --> sys
    datetime(("datetime"))
    examples_experiment_twitter_gpt_example_twitter_simulation_py --> datetime
    pathlib(("pathlib"))
    examples_experiment_twitter_gpt_example_twitter_simulation_py --> pathlib
    typing(("typing"))
    examples_experiment_twitter_gpt_example_twitter_simulation_py --> typing
    pandas(("pandas"))
    examples_experiment_twitter_gpt_example_twitter_simulation_py --> pandas
    colorama(("colorama"))
    examples_experiment_twitter_gpt_example_twitter_simulation_py --> colorama
    yaml(("yaml"))
    examples_experiment_twitter_gpt_example_twitter_simulation_py --> yaml
    camel_models(("camel.models"))
    examples_experiment_twitter_gpt_example_twitter_simulation_py --> camel_models
    camel_types(("camel.types"))
    examples_experiment_twitter_gpt_example_twitter_simulation_py --> camel_types
    oasis_clock_clock(("oasis.clock.clock"))
    examples_experiment_twitter_gpt_example_twitter_simulation_py --> oasis_clock_clock
    oasis_social_agent_agents_generator(("oasis.social_agent.agents_generator"))
    examples_experiment_twitter_gpt_example_twitter_simulation_py --> oasis_social_agent_agents_generator
    oasis_social_platform_channel(("oasis.social_platform.channel"))
    examples_experiment_twitter_gpt_example_twitter_simulation_py --> oasis_social_platform_channel
    oasis_social_platform_platform(("oasis.social_platform.platform"))
    examples_experiment_twitter_gpt_example_twitter_simulation_py --> oasis_social_platform_platform
    oasis_social_platform_typing(("oasis.social_platform.typing"))
    examples_experiment_twitter_gpt_example_twitter_simulation_py --> oasis_social_platform_typing
    examples_experiment_reddit_emall_demo_emall_simulation_py["examples/experiment/reddit_emall_demo/emall_simulation.py"]
    click examples_experiment_reddit_emall_demo_emall_simulation_py "https://github.com/camel-ai/oasis/blob/main/examples/experiment/reddit_emall_demo/emall_simulation.py" "View source"
    __future__(("__future__"))
    examples_experiment_reddit_emall_demo_emall_simulation_py --> __future__
    argparse(("argparse"))
    examples_experiment_reddit_emall_demo_emall_simulation_py --> argparse
    asyncio(("asyncio"))
    examples_experiment_reddit_emall_demo_emall_simulation_py --> asyncio
    json(("json"))
    examples_experiment_reddit_emall_demo_emall_simulation_py --> json
    logging(("logging"))
    examples_experiment_reddit_emall_demo_emall_simulation_py --> logging
    os(("os"))
    examples_experiment_reddit_emall_demo_emall_simulation_py --> os
    random(("random"))
    examples_experiment_reddit_emall_demo_emall_simulation_py --> random
    sys(("sys"))
    examples_experiment_reddit_emall_demo_emall_simulation_py --> sys
    datetime(("datetime"))
    examples_experiment_reddit_emall_demo_emall_simulation_py --> datetime
    typing(("typing"))
    examples_experiment_reddit_emall_demo_emall_simulation_py --> typing
    colorama(("colorama"))
    examples_experiment_reddit_emall_demo_emall_simulation_py --> colorama
    yaml(("yaml"))
    examples_experiment_reddit_emall_demo_emall_simulation_py --> yaml
    camel_models(("camel.models"))
    examples_experiment_reddit_emall_demo_emall_simulation_py --> camel_models
    camel_types(("camel.types"))
    examples_experiment_reddit_emall_demo_emall_simulation_py --> camel_types
    oasis_clock_clock(("oasis.clock.clock"))
    examples_experiment_reddit_emall_demo_emall_simulation_py --> oasis_clock_clock
    oasis_social_agent_agents_generator(("oasis.social_agent.agents_generator"))
    examples_experiment_reddit_emall_demo_emall_simulation_py --> oasis_social_agent_agents_generator
    oasis_social_platform_channel(("oasis.social_platform.channel"))
    examples_experiment_reddit_emall_demo_emall_simulation_py --> oasis_social_platform_channel
    oasis_social_platform_platform(("oasis.social_platform.platform"))
    examples_experiment_reddit_emall_demo_emall_simulation_py --> oasis_social_platform_platform
    oasis_social_platform_typing(("oasis.social_platform.typing"))
    examples_experiment_reddit_emall_demo_emall_simulation_py --> oasis_social_platform_typing
    examples_experiment_twitter_simulation_1M_agents_twitter_simulation_1m_py["examples/experiment/twitter_simulation_1M_agents/twitter_simulation_1m.py"]
    click examples_experiment_twitter_simulation_1M_agents_twitter_simulation_1m_py "https://github.com/camel-ai/oasis/blob/main/examples/experiment/twitter_simulation_1M_agents/twitter_simulation_1m.py" "View source"
    __future__(("__future__"))
    examples_experiment_twitter_simulation_1M_agents_twitter_simulation_1m_py --> __future__
    argparse(("argparse"))
    examples_experiment_twitter_simulation_1M_agents_twitter_simulation_1m_py --> argparse
    asyncio(("asyncio"))
    examples_experiment_twitter_simulation_1M_agents_twitter_simulation_1m_py --> asyncio
    logging(("logging"))
    examples_experiment_twitter_simulation_1M_agents_twitter_simulation_1m_py --> logging
    os(("os"))
    examples_experiment_twitter_simulation_1M_agents_twitter_simulation_1m_py --> os
    random(("random"))
    examples_experiment_twitter_simulation_1M_agents_twitter_simulation_1m_py --> random
    sys(("sys"))
    examples_experiment_twitter_simulation_1M_agents_twitter_simulation_1m_py --> sys
    datetime(("datetime"))
    examples_experiment_twitter_simulation_1M_agents_twitter_simulation_1m_py --> datetime
    typing(("typing"))
    examples_experiment_twitter_simulation_1M_agents_twitter_simulation_1m_py --> typing
    pandas(("pandas"))
    examples_experiment_twitter_simulation_1M_agents_twitter_simulation_1m_py --> pandas
    camel_models(("camel.models"))
    examples_experiment_twitter_simulation_1M_agents_twitter_simulation_1m_py --> camel_models
    camel_types(("camel.types"))
    examples_experiment_twitter_simulation_1M_agents_twitter_simulation_1m_py --> camel_types
    colorama(("colorama"))
    examples_experiment_twitter_simulation_1M_agents_twitter_simulation_1m_py --> colorama
    yaml(("yaml"))
    examples_experiment_twitter_simulation_1M_agents_twitter_simulation_1m_py --> yaml
    utils(("utils"))
    examples_experiment_twitter_simulation_1M_agents_twitter_simulation_1m_py --> utils
    oasis_clock_clock(("oasis.clock.clock"))
    examples_experiment_twitter_simulation_1M_agents_twitter_simulation_1m_py --> oasis_clock_clock
    oasis_social_agent_agents_generator(("oasis.social_agent.agents_generator"))
    examples_experiment_twitter_simulation_1M_agents_twitter_simulation_1m_py --> oasis_social_agent_agents_generator
    oasis_social_platform_channel(("oasis.social_platform.channel"))
    examples_experiment_twitter_simulation_1M_agents_twitter_simulation_1m_py --> oasis_social_platform_channel
    oasis_social_platform_platform(("oasis.social_platform.platform"))
    examples_experiment_twitter_simulation_1M_agents_twitter_simulation_1m_py --> oasis_social_platform_platform
    oasis_social_platform_typing(("oasis.social_platform.typing"))
    examples_experiment_twitter_simulation_1M_agents_twitter_simulation_1m_py --> oasis_social_platform_typing
    examples_experiment_reddit_gpt_example_reddit_simulation_gpt_py["examples/experiment/reddit_gpt_example/reddit_simulation_gpt.py"]
    click examples_experiment_reddit_gpt_example_reddit_simulation_gpt_py "https://github.com/camel-ai/oasis/blob/main/examples/experiment/reddit_gpt_example/reddit_simulation_gpt.py" "View source"
    __future__(("__future__"))
    examples_experiment_reddit_gpt_example_reddit_simulation_gpt_py --> __future__
    argparse(("argparse"))
    examples_experiment_reddit_gpt_example_reddit_simulation_gpt_py --> argparse
    asyncio(("asyncio"))
    examples_experiment_reddit_gpt_example_reddit_simulation_gpt_py --> asyncio
    json(("json"))
    examples_experiment_reddit_gpt_example_reddit_simulation_gpt_py --> json
    logging(("logging"))
    examples_experiment_reddit_gpt_example_reddit_simulation_gpt_py --> logging
    os(("os"))
    examples_experiment_reddit_gpt_example_reddit_simulation_gpt_py --> os
    random(("random"))
    examples_experiment_reddit_gpt_example_reddit_simulation_gpt_py --> random
    sys(("sys"))
    examples_experiment_reddit_gpt_example_reddit_simulation_gpt_py --> sys
    datetime(("datetime"))
    examples_experiment_reddit_gpt_example_reddit_simulation_gpt_py --> datetime
    typing(("typing"))
    examples_experiment_reddit_gpt_example_reddit_simulation_gpt_py --> typing
    colorama(("colorama"))
    examples_experiment_reddit_gpt_example_reddit_simulation_gpt_py --> colorama
    yaml(("yaml"))
    examples_experiment_reddit_gpt_example_reddit_simulation_gpt_py --> yaml
    camel_models(("camel.models"))
    examples_experiment_reddit_gpt_example_reddit_simulation_gpt_py --> camel_models
    camel_types(("camel.types"))
    examples_experiment_reddit_gpt_example_reddit_simulation_gpt_py --> camel_types
    oasis_clock_clock(("oasis.clock.clock"))
    examples_experiment_reddit_gpt_example_reddit_simulation_gpt_py --> oasis_clock_clock
    oasis_social_agent_agents_generator(("oasis.social_agent.agents_generator"))
    examples_experiment_reddit_gpt_example_reddit_simulation_gpt_py --> oasis_social_agent_agents_generator
    oasis_social_platform_channel(("oasis.social_platform.channel"))
    examples_experiment_reddit_gpt_example_reddit_simulation_gpt_py --> oasis_social_platform_channel
    oasis_social_platform_platform(("oasis.social_platform.platform"))
    examples_experiment_reddit_gpt_example_reddit_simulation_gpt_py --> oasis_social_platform_platform
    oasis_social_platform_typing(("oasis.social_platform.typing"))
    examples_experiment_reddit_gpt_example_reddit_simulation_gpt_py --> oasis_social_platform_typing
    examples_experiment_reddit_simulation_align_with_human_reddit_simulation_align_with_human_py["examples/experiment/reddit_simulation_align_with_human/reddit_simulation_align_with_human.py"]
    click examples_experiment_reddit_simulation_align_with_human_reddit_simulation_align_with_human_py "https://github.com/camel-ai/oasis/blob/main/examples/experiment/reddit_simulation_align_with_human/reddit_simulation_align_with_human.py" "View source"
    __future__(("__future__"))
    examples_experiment_reddit_simulation_align_with_human_reddit_simulation_align_with_human_py --> __future__
    argparse(("argparse"))
    examples_experiment_reddit_simulation_align_with_human_reddit_simulation_align_with_human_py --> argparse
    asyncio(("asyncio"))
    examples_experiment_reddit_simulation_align_with_human_reddit_simulation_align_with_human_py --> asyncio
    json(("json"))
    examples_experiment_reddit_simulation_align_with_human_reddit_simulation_align_with_human_py --> json
    logging(("logging"))
    examples_experiment_reddit_simulation_align_with_human_reddit_simulation_align_with_human_py --> logging
    os(("os"))
    examples_experiment_reddit_simulation_align_with_human_reddit_simulation_align_with_human_py --> os
    random(("random"))
    examples_experiment_reddit_simulation_align_with_human_reddit_simulation_align_with_human_py --> random
    sys(("sys"))
    examples_experiment_reddit_simulation_align_with_human_reddit_simulation_align_with_human_py --> sys
    datetime(("datetime"))
    examples_experiment_reddit_simulation_align_with_human_reddit_simulation_align_with_human_py --> datetime
    typing(("typing"))
    examples_experiment_reddit_simulation_align_with_human_reddit_simulation_align_with_human_py --> typing
    camel_models(("camel.models"))
    examples_experiment_reddit_simulation_align_with_human_reddit_simulation_align_with_human_py --> camel_models
    camel_types(("camel.types"))
    examples_experiment_reddit_simulation_align_with_human_reddit_simulation_align_with_human_py --> camel_types
    yaml(("yaml"))
    examples_experiment_reddit_simulation_align_with_human_reddit_simulation_align_with_human_py --> yaml
    utils(("utils"))
    examples_experiment_reddit_simulation_align_with_human_reddit_simulation_align_with_human_py --> utils
    oasis_clock_clock(("oasis.clock.clock"))
    examples_experiment_reddit_simulation_align_with_human_reddit_simulation_align_with_human_py --> oasis_clock_clock
    oasis_social_agent_agents_generator(("oasis.social_agent.agents_generator"))
    examples_experiment_reddit_simulation_align_with_human_reddit_simulation_align_with_human_py --> oasis_social_agent_agents_generator
    oasis_social_platform_channel(("oasis.social_platform.channel"))
    examples_experiment_reddit_simulation_align_with_human_reddit_simulation_align_with_human_py --> oasis_social_platform_channel
    oasis_social_platform_platform(("oasis.social_platform.platform"))
    examples_experiment_reddit_simulation_align_with_human_reddit_simulation_align_with_human_py --> oasis_social_platform_platform
    oasis_social_platform_typing(("oasis.social_platform.typing"))
    examples_experiment_reddit_simulation_align_with_human_reddit_simulation_align_with_human_py --> oasis_social_platform_typing
    examples_experiment_reddit_simulation_align_with_human___init___py["examples/experiment/reddit_simulation_align_with_human/__init__.py"]
    click examples_experiment_reddit_simulation_align_with_human___init___py "https://github.com/camel-ai/oasis/blob/main/examples/experiment/reddit_simulation_align_with_human/__init__.py" "View source"
    examples_experiment_twitter_simulation_align_with_real_world_twitter_simulation_large_py["examples/experiment/twitter_simulation/align_with_real_world/twitter_simulation_large.py"]
    click examples_experiment_twitter_simulation_align_with_real_world_twitter_simulation_large_py "https://github.com/camel-ai/oasis/blob/main/examples/experiment/twitter_simulation/align_with_real_world/twitter_simulation_large.py" "View source"
    __future__(("__future__"))
    examples_experiment_twitter_simulation_align_with_real_world_twitter_simulation_large_py --> __future__
    argparse(("argparse"))
    examples_experiment_twitter_simulation_align_with_real_world_twitter_simulation_large_py --> argparse
    asyncio(("asyncio"))
    examples_experiment_twitter_simulation_align_with_real_world_twitter_simulation_large_py --> asyncio
    logging(("logging"))
    examples_experiment_twitter_simulation_align_with_real_world_twitter_simulation_large_py --> logging
    os(("os"))
    examples_experiment_twitter_simulation_align_with_real_world_twitter_simulation_large_py --> os
    random(("random"))
    examples_experiment_twitter_simulation_align_with_real_world_twitter_simulation_large_py --> random
    sys(("sys"))
    examples_experiment_twitter_simulation_align_with_real_world_twitter_simulation_large_py --> sys
    datetime(("datetime"))
    examples_experiment_twitter_simulation_align_with_real_world_twitter_simulation_large_py --> datetime
    pathlib(("pathlib"))
    examples_experiment_twitter_simulation_align_with_real_world_twitter_simulation_large_py --> pathlib
    typing(("typing"))
    examples_experiment_twitter_simulation_align_with_real_world_twitter_simulation_large_py --> typing
    pandas(("pandas"))
    examples_experiment_twitter_simulation_align_with_real_world_twitter_simulation_large_py --> pandas
    camel_models(("camel.models"))
    examples_experiment_twitter_simulation_align_with_real_world_twitter_simulation_large_py --> camel_models
    camel_types(("camel.types"))
    examples_experiment_twitter_simulation_align_with_real_world_twitter_simulation_large_py --> camel_types
    colorama(("colorama"))
    examples_experiment_twitter_simulation_align_with_real_world_twitter_simulation_large_py --> colorama
    yaml(("yaml"))
    examples_experiment_twitter_simulation_align_with_real_world_twitter_simulation_large_py --> yaml
    utils(("utils"))
    examples_experiment_twitter_simulation_align_with_real_world_twitter_simulation_large_py --> utils
    oasis_clock_clock(("oasis.clock.clock"))
    examples_experiment_twitter_simulation_align_with_real_world_twitter_simulation_large_py --> oasis_clock_clock
    oasis_social_agent_agents_generator(("oasis.social_agent.agents_generator"))
    examples_experiment_twitter_simulation_align_with_real_world_twitter_simulation_large_py --> oasis_social_agent_agents_generator
    oasis_social_platform_channel(("oasis.social_platform.channel"))
    examples_experiment_twitter_simulation_align_with_real_world_twitter_simulation_large_py --> oasis_social_platform_channel
    oasis_social_platform_platform(("oasis.social_platform.platform"))
    examples_experiment_twitter_simulation_align_with_real_world_twitter_simulation_large_py --> oasis_social_platform_platform
    oasis_social_platform_typing(("oasis.social_platform.typing"))
    examples_experiment_twitter_simulation_align_with_real_world_twitter_simulation_large_py --> oasis_social_platform_typing
    examples_experiment_twitter_simulation_group_polarization_twitter_simulation_group_polar_py["examples/experiment/twitter_simulation/group_polarization/twitter_simulation_group_polar.py"]
    click examples_experiment_twitter_simulation_group_polarization_twitter_simulation_group_polar_py "https://github.com/camel-ai/oasis/blob/main/examples/experiment/twitter_simulation/group_polarization/twitter_simulation_group_polar.py" "View source"
    __future__(("__future__"))
    examples_experiment_twitter_simulation_group_polarization_twitter_simulation_group_polar_py --> __future__
    argparse(("argparse"))
    examples_experiment_twitter_simulation_group_polarization_twitter_simulation_group_polar_py --> argparse
    asyncio(("asyncio"))
    examples_experiment_twitter_simulation_group_polarization_twitter_simulation_group_polar_py --> asyncio
    logging(("logging"))
    examples_experiment_twitter_simulation_group_polarization_twitter_simulation_group_polar_py --> logging
    os(("os"))
    examples_experiment_twitter_simulation_group_polarization_twitter_simulation_group_polar_py --> os
    random(("random"))
    examples_experiment_twitter_simulation_group_polarization_twitter_simulation_group_polar_py --> random
    sys(("sys"))
    examples_experiment_twitter_simulation_group_polarization_twitter_simulation_group_polar_py --> sys
    datetime(("datetime"))
    examples_experiment_twitter_simulation_group_polarization_twitter_simulation_group_polar_py --> datetime
    typing(("typing"))
    examples_experiment_twitter_simulation_group_polarization_twitter_simulation_group_polar_py --> typing
    pandas(("pandas"))
    examples_experiment_twitter_simulation_group_polarization_twitter_simulation_group_polar_py --> pandas
    camel_models(("camel.models"))
    examples_experiment_twitter_simulation_group_polarization_twitter_simulation_group_polar_py --> camel_models
    camel_types(("camel.types"))
    examples_experiment_twitter_simulation_group_polarization_twitter_simulation_group_polar_py --> camel_types
    colorama(("colorama"))
    examples_experiment_twitter_simulation_group_polarization_twitter_simulation_group_polar_py --> colorama
    yaml(("yaml"))
    examples_experiment_twitter_simulation_group_polarization_twitter_simulation_group_polar_py --> yaml
    utils(("utils"))
    examples_experiment_twitter_simulation_group_polarization_twitter_simulation_group_polar_py --> utils
    oasis_clock_clock(("oasis.clock.clock"))
    examples_experiment_twitter_simulation_group_polarization_twitter_simulation_group_polar_py --> oasis_clock_clock
    oasis_social_agent_agents_generator(("oasis.social_agent.agents_generator"))
    examples_experiment_twitter_simulation_group_polarization_twitter_simulation_group_polar_py --> oasis_social_agent_agents_generator
    oasis_social_platform_channel(("oasis.social_platform.channel"))
    examples_experiment_twitter_simulation_group_polarization_twitter_simulation_group_polar_py --> oasis_social_platform_channel
    oasis_social_platform_platform(("oasis.social_platform.platform"))
    examples_experiment_twitter_simulation_group_polarization_twitter_simulation_group_polar_py --> oasis_social_platform_platform
    oasis_social_platform_typing(("oasis.social_platform.typing"))
    examples_experiment_twitter_simulation_group_polarization_twitter_simulation_group_polar_py --> oasis_social_platform_typing
    oasis_social_platform_channel_py["oasis/social_platform/channel.py"]
    click oasis_social_platform_channel_py "https://github.com/camel-ai/oasis/blob/main/oasis/social_platform/channel.py" "View source"
    asyncio(("asyncio"))
    oasis_social_platform_channel_py --> asyncio
    uuid(("uuid"))
    oasis_social_platform_channel_py --> uuid
    oasis_social_platform_recsys_py["oasis/social_platform/recsys.py"]
    click oasis_social_platform_recsys_py "https://github.com/camel-ai/oasis/blob/main/oasis/social_platform/recsys.py" "View source"
    heapq(("heapq"))
    oasis_social_platform_recsys_py --> heapq
    logging(("logging"))
    oasis_social_platform_recsys_py --> logging
    random(("random"))
    oasis_social_platform_recsys_py --> random
    time(("time"))
    oasis_social_platform_recsys_py --> time
    ast(("ast"))
    oasis_social_platform_recsys_py --> ast
    datetime(("datetime"))
    oasis_social_platform_recsys_py --> datetime
    math(("math"))
    oasis_social_platform_recsys_py --> math
    typing(("typing"))
    oasis_social_platform_recsys_py --> typing
    numpy(("numpy"))
    oasis_social_platform_recsys_py --> numpy
    torch(("torch"))
    oasis_social_platform_recsys_py --> torch
    sentence_transformers(("sentence_transformers"))
    oasis_social_platform_recsys_py --> sentence_transformers
    sklearn_feature_extraction_text(("sklearn.feature_extraction.text"))
    oasis_social_platform_recsys_py --> sklearn_feature_extraction_text
    sklearn_metrics_pairwise(("sklearn.metrics.pairwise"))
    oasis_social_platform_recsys_py --> sklearn_metrics_pairwise
    process_recsys_posts(("process_recsys_posts"))
    oasis_social_platform_recsys_py --> process_recsys_posts
    typing(("typing"))
    oasis_social_platform_recsys_py --> typing
    transformers(("transformers"))
    oasis_social_platform_recsys_py --> transformers
    transformers(("transformers"))
    oasis_social_platform_recsys_py --> transformers
    pdb(("pdb"))
    oasis_social_platform_recsys_py --> pdb
    pdb(("pdb"))
    oasis_social_platform_recsys_py --> pdb
    oasis_social_platform_process_recsys_posts_py["oasis/social_platform/process_recsys_posts.py"]
    click oasis_social_platform_process_recsys_posts_py "https://github.com/camel-ai/oasis/blob/main/oasis/social_platform/process_recsys_posts.py" "View source"
    typing(("typing"))
    oasis_social_platform_process_recsys_posts_py --> typing
    torch(("torch"))
    oasis_social_platform_process_recsys_posts_py --> torch
    camel_embeddings(("camel.embeddings"))
    oasis_social_platform_process_recsys_posts_py --> camel_embeddings
    camel_types(("camel.types"))
    oasis_social_platform_process_recsys_posts_py --> camel_types
    transformers(("transformers"))
    oasis_social_platform_process_recsys_posts_py --> transformers
    oasis_social_platform_database_py["oasis/social_platform/database.py"]
    click oasis_social_platform_database_py "https://github.com/camel-ai/oasis/blob/main/oasis/social_platform/database.py" "View source"
    __future__(("__future__"))
    oasis_social_platform_database_py --> __future__
    os(("os"))
    oasis_social_platform_database_py --> os
    os_path(("os.path"))
    oasis_social_platform_database_py --> os_path
    sqlite3(("sqlite3"))
    oasis_social_platform_database_py --> sqlite3
    typing(("typing"))
    oasis_social_platform_database_py --> typing
    oasis_social_platform___init___py["oasis/social_platform/__init__.py"]
    click oasis_social_platform___init___py "https://github.com/camel-ai/oasis/blob/main/oasis/social_platform/__init__.py" "View source"
    channel(("channel"))
    oasis_social_platform___init___py --> channel
    platform(("platform"))
    oasis_social_platform___init___py --> platform
    oasis_social_platform_platform_utils_py["oasis/social_platform/platform_utils.py"]
    click oasis_social_platform_platform_utils_py "https://github.com/camel-ai/oasis/blob/main/oasis/social_platform/platform_utils.py" "View source"
    json(("json"))
    oasis_social_platform_platform_utils_py --> json
    datetime(("datetime"))
    oasis_social_platform_platform_utils_py --> datetime
    oasis_social_platform_typing(("oasis.social_platform.typing"))
    oasis_social_platform_platform_utils_py --> oasis_social_platform_typing
    oasis_social_platform_typing_py["oasis/social_platform/typing.py"]
    click oasis_social_platform_typing_py "https://github.com/camel-ai/oasis/blob/main/oasis/social_platform/typing.py" "View source"
    enum(("enum"))
    oasis_social_platform_typing_py --> enum
    oasis_social_platform_platform_py["oasis/social_platform/platform.py"]
    click oasis_social_platform_platform_py "https://github.com/camel-ai/oasis/blob/main/oasis/social_platform/platform.py" "View source"
    __future__(("__future__"))
    oasis_social_platform_platform_py --> __future__
    asyncio(("asyncio"))
    oasis_social_platform_platform_py --> asyncio
    logging(("logging"))
    oasis_social_platform_platform_py --> logging
    os(("os"))
    oasis_social_platform_platform_py --> os
    random(("random"))
    oasis_social_platform_platform_py --> random
    sqlite3(("sqlite3"))
    oasis_social_platform_platform_py --> sqlite3
    sys(("sys"))
    oasis_social_platform_platform_py --> sys
    datetime(("datetime"))
    oasis_social_platform_platform_py --> datetime
    typing(("typing"))
    oasis_social_platform_platform_py --> typing
    oasis_clock_clock(("oasis.clock.clock"))
    oasis_social_platform_platform_py --> oasis_clock_clock
    oasis_social_platform_channel(("oasis.social_platform.channel"))
    oasis_social_platform_platform_py --> oasis_social_platform_channel
    oasis_social_platform_database(("oasis.social_platform.database"))
    oasis_social_platform_platform_py --> oasis_social_platform_database
    oasis_social_platform_platform_utils(("oasis.social_platform.platform_utils"))
    oasis_social_platform_platform_py --> oasis_social_platform_platform_utils
    oasis_social_platform_recsys(("oasis.social_platform.recsys"))
    oasis_social_platform_platform_py --> oasis_social_platform_recsys
    oasis_social_platform_typing(("oasis.social_platform.typing"))
    oasis_social_platform_platform_py --> oasis_social_platform_typing
    oasis_testing___init___py["oasis/testing/__init__.py"]
    click oasis_testing___init___py "https://github.com/camel-ai/oasis/blob/main/oasis/testing/__init__.py" "View source"
    oasis_testing_show_db_py["oasis/testing/show_db.py"]
    click oasis_testing_show_db_py "https://github.com/camel-ai/oasis/blob/main/oasis/testing/show_db.py" "View source"
    logging(("logging"))
    oasis_testing_show_db_py --> logging
    sqlite3(("sqlite3"))
    oasis_testing_show_db_py --> sqlite3
    datetime(("datetime"))
    oasis_testing_show_db_py --> datetime
    oasis_environment___init___py["oasis/environment/__init__.py"]
    click oasis_environment___init___py "https://github.com/camel-ai/oasis/blob/main/oasis/environment/__init__.py" "View source"
    oasis_environment_env_action_py["oasis/environment/env_action.py"]
    click oasis_environment_env_action_py "https://github.com/camel-ai/oasis/blob/main/oasis/environment/env_action.py" "View source"
    dataclasses(("dataclasses"))
    oasis_environment_env_action_py --> dataclasses
    typing(("typing"))
    oasis_environment_env_action_py --> typing
    oasis_social_platform_typing(("oasis.social_platform.typing"))
    oasis_environment_env_action_py --> oasis_social_platform_typing
    oasis_environment_make_py["oasis/environment/make.py"]
    click oasis_environment_make_py "https://github.com/camel-ai/oasis/blob/main/oasis/environment/make.py" "View source"
    oasis_environment_env(("oasis.environment.env"))
    oasis_environment_make_py --> oasis_environment_env
    oasis_environment_env_py["oasis/environment/env.py"]
    click oasis_environment_env_py "https://github.com/camel-ai/oasis/blob/main/oasis/environment/env.py" "View source"
    asyncio(("asyncio"))
    oasis_environment_env_py --> asyncio
    logging(("logging"))
    oasis_environment_env_py --> logging
    os(("os"))
    oasis_environment_env_py --> os
    datetime(("datetime"))
    oasis_environment_env_py --> datetime
    typing(("typing"))
    oasis_environment_env_py --> typing
    oasis_environment_env_action(("oasis.environment.env_action"))
    oasis_environment_env_py --> oasis_environment_env_action
    oasis_social_agent_agent(("oasis.social_agent.agent"))
    oasis_environment_env_py --> oasis_social_agent_agent
    oasis_social_agent_agent_graph(("oasis.social_agent.agent_graph"))
    oasis_environment_env_py --> oasis_social_agent_agent_graph
    oasis_social_agent_agents_generator(("oasis.social_agent.agents_generator"))
    oasis_environment_env_py --> oasis_social_agent_agents_generator
    oasis_social_platform_channel(("oasis.social_platform.channel"))
    oasis_environment_env_py --> oasis_social_platform_channel
    oasis_social_platform_platform(("oasis.social_platform.platform"))
    oasis_environment_env_py --> oasis_social_platform_platform
    oasis_social_platform_typing(("oasis.social_platform.typing"))
    oasis_environment_env_py --> oasis_social_platform_typing
    oasis_social_agent_agent_environment_py["oasis/social_agent/agent_environment.py"]
    click oasis_social_agent_agent_environment_py "https://github.com/camel-ai/oasis/blob/main/oasis/social_agent/agent_environment.py" "View source"
    __future__(("__future__"))
    oasis_social_agent_agent_environment_py --> __future__
    json(("json"))
    oasis_social_agent_agent_environment_py --> json
    sqlite3(("sqlite3"))
    oasis_social_agent_agent_environment_py --> sqlite3
    abc(("abc"))
    oasis_social_agent_agent_environment_py --> abc
    string(("string"))
    oasis_social_agent_agent_environment_py --> string
    oasis_social_agent_agent_action(("oasis.social_agent.agent_action"))
    oasis_social_agent_agent_environment_py --> oasis_social_agent_agent_action
    oasis_social_platform_database(("oasis.social_platform.database"))
    oasis_social_agent_agent_environment_py --> oasis_social_platform_database
    oasis_social_agent___init___py["oasis/social_agent/__init__.py"]
    click oasis_social_agent___init___py "https://github.com/camel-ai/oasis/blob/main/oasis/social_agent/__init__.py" "View source"
    agent(("agent"))
    oasis_social_agent___init___py --> agent
    agent_graph(("agent_graph"))
    oasis_social_agent___init___py --> agent_graph
    agents_generator(("agents_generator"))
    oasis_social_agent___init___py --> agents_generator
    oasis_social_agent_agents_generator_py["oasis/social_agent/agents_generator.py"]
    click oasis_social_agent_agents_generator_py "https://github.com/camel-ai/oasis/blob/main/oasis/social_agent/agents_generator.py" "View source"
    __future__(("__future__"))
    oasis_social_agent_agents_generator_py --> __future__
    ast(("ast"))
    oasis_social_agent_agents_generator_py --> ast
    asyncio(("asyncio"))
    oasis_social_agent_agents_generator_py --> asyncio
    json(("json"))
    oasis_social_agent_agents_generator_py --> json
    typing(("typing"))
    oasis_social_agent_agents_generator_py --> typing
    pandas(("pandas"))
    oasis_social_agent_agents_generator_py --> pandas
    tqdm(("tqdm"))
    oasis_social_agent_agents_generator_py --> tqdm
    camel_memories(("camel.memories"))
    oasis_social_agent_agents_generator_py --> camel_memories
    camel_messages(("camel.messages"))
    oasis_social_agent_agents_generator_py --> camel_messages
    camel_models(("camel.models"))
    oasis_social_agent_agents_generator_py --> camel_models
    camel_types(("camel.types"))
    oasis_social_agent_agents_generator_py --> camel_types
    oasis_social_agent(("oasis.social_agent"))
    oasis_social_agent_agents_generator_py --> oasis_social_agent
    oasis_social_platform(("oasis.social_platform"))
    oasis_social_agent_agents_generator_py --> oasis_social_platform
    oasis_social_platform_config(("oasis.social_platform.config"))
    oasis_social_agent_agents_generator_py --> oasis_social_platform_config
    oasis_social_platform_typing(("oasis.social_platform.typing"))
    oasis_social_agent_agents_generator_py --> oasis_social_platform_typing
    oasis_social_agent_agent_py["oasis/social_agent/agent.py"]
    click oasis_social_agent_agent_py "https://github.com/camel-ai/oasis/blob/main/oasis/social_agent/agent.py" "View source"
    __future__(("__future__"))
    oasis_social_agent_agent_py --> __future__
    inspect(("inspect"))
    oasis_social_agent_agent_py --> inspect
    logging(("logging"))
    oasis_social_agent_agent_py --> logging
    sys(("sys"))
    oasis_social_agent_agent_py --> sys
    datetime(("datetime"))
    oasis_social_agent_agent_py --> datetime
    typing(("typing"))
    oasis_social_agent_agent_py --> typing
    camel_agents(("camel.agents"))
    oasis_social_agent_agent_py --> camel_agents
    camel_messages(("camel.messages"))
    oasis_social_agent_agent_py --> camel_messages
    camel_models(("camel.models"))
    oasis_social_agent_agent_py --> camel_models
    camel_prompts(("camel.prompts"))
    oasis_social_agent_agent_py --> camel_prompts
    camel_toolkits(("camel.toolkits"))
    oasis_social_agent_agent_py --> camel_toolkits
    camel_types(("camel.types"))
    oasis_social_agent_agent_py --> camel_types
    oasis_social_agent_agent_action(("oasis.social_agent.agent_action"))
    oasis_social_agent_agent_py --> oasis_social_agent_agent_action
    oasis_social_agent_agent_environment(("oasis.social_agent.agent_environment"))
    oasis_social_agent_agent_py --> oasis_social_agent_agent_environment
    oasis_social_platform(("oasis.social_platform"))
    oasis_social_agent_agent_py --> oasis_social_platform
    oasis_social_platform_config(("oasis.social_platform.config"))
    oasis_social_agent_agent_py --> oasis_social_platform_config
    oasis_social_platform_typing(("oasis.social_platform.typing"))
    oasis_social_agent_agent_py --> oasis_social_platform_typing
    oasis_social_agent(("oasis.social_agent"))
    oasis_social_agent_agent_py --> oasis_social_agent
    oasis_social_agent_agent_graph_py["oasis/social_agent/agent_graph.py"]
    click oasis_social_agent_agent_graph_py "https://github.com/camel-ai/oasis/blob/main/oasis/social_agent/agent_graph.py" "View source"
    __future__(("__future__"))
    oasis_social_agent_agent_graph_py --> __future__
    typing(("typing"))
    oasis_social_agent_agent_graph_py --> typing
    igraph(("igraph"))
    oasis_social_agent_agent_graph_py --> igraph
    neo4j(("neo4j"))
    oasis_social_agent_agent_graph_py --> neo4j
    oasis_social_agent_agent(("oasis.social_agent.agent"))
    oasis_social_agent_agent_graph_py --> oasis_social_agent_agent
    oasis_social_platform_config(("oasis.social_platform.config"))
    oasis_social_agent_agent_graph_py --> oasis_social_platform_config
    oasis_social_agent_agent_action_py["oasis/social_agent/agent_action.py"]
    click oasis_social_agent_agent_action_py "https://github.com/camel-ai/oasis/blob/main/oasis/social_agent/agent_action.py" "View source"
    typing(("typing"))
    oasis_social_agent_agent_action_py --> typing
    camel_toolkits(("camel.toolkits"))
    oasis_social_agent_agent_action_py --> camel_toolkits
    oasis_social_platform_channel(("oasis.social_platform.channel"))
    oasis_social_agent_agent_action_py --> oasis_social_platform_channel
    oasis_social_platform_typing(("oasis.social_platform.typing"))
    oasis_social_agent_agent_action_py --> oasis_social_platform_typing
    oasis_clock_clock_py["oasis/clock/clock.py"]
    click oasis_clock_clock_py "https://github.com/camel-ai/oasis/blob/main/oasis/clock/clock.py" "View source"
    datetime(("datetime"))
    oasis_clock_clock_py --> datetime
    oasis_clock___init___py["oasis/clock/__init__.py"]
    click oasis_clock___init___py "https://github.com/camel-ai/oasis/blob/main/oasis/clock/__init__.py" "View source"
    clock(("clock"))
    oasis_clock___init___py --> clock
    oasis_social_platform_config_neo4j_py["oasis/social_platform/config/neo4j.py"]
    click oasis_social_platform_config_neo4j_py "https://github.com/camel-ai/oasis/blob/main/oasis/social_platform/config/neo4j.py" "View source"
    dataclasses(("dataclasses"))
    oasis_social_platform_config_neo4j_py --> dataclasses
    oasis_social_platform_config___init___py["oasis/social_platform/config/__init__.py"]
    click oasis_social_platform_config___init___py "https://github.com/camel-ai/oasis/blob/main/oasis/social_platform/config/__init__.py" "View source"
    neo4j(("neo4j"))
    oasis_social_platform_config___init___py --> neo4j
    user(("user"))
    oasis_social_platform_config___init___py --> user
    oasis_social_platform_config_user_py["oasis/social_platform/config/user.py"]
    click oasis_social_platform_config_user_py "https://github.com/camel-ai/oasis/blob/main/oasis/social_platform/config/user.py" "View source"
    warnings(("warnings"))
    oasis_social_platform_config_user_py --> warnings
    dataclasses(("dataclasses"))
    oasis_social_platform_config_user_py --> dataclasses
    typing(("typing"))
    oasis_social_platform_config_user_py --> typing
    camel_prompts(("camel.prompts"))
    oasis_social_platform_config_user_py --> camel_prompts
    visualization_reddit_simulation_counterfactual_code_analysis_couterfact_py["visualization/reddit_simulation_counterfactual/code/analysis_couterfact.py"]
    click visualization_reddit_simulation_counterfactual_code_analysis_couterfact_py "https://github.com/camel-ai/oasis/blob/main/visualization/reddit_simulation_counterfactual/code/analysis_couterfact.py" "View source"
    asyncio(("asyncio"))
    visualization_reddit_simulation_counterfactual_code_analysis_couterfact_py --> asyncio
    json(("json"))
    visualization_reddit_simulation_counterfactual_code_analysis_couterfact_py --> json
    os(("os"))
    visualization_reddit_simulation_counterfactual_code_analysis_couterfact_py --> os
    sqlite3(("sqlite3"))
    visualization_reddit_simulation_counterfactual_code_analysis_couterfact_py --> sqlite3
    aiohttp(("aiohttp"))
    visualization_reddit_simulation_counterfactual_code_analysis_couterfact_py --> aiohttp
    matplotlib_pyplot(("matplotlib.pyplot"))
    visualization_reddit_simulation_counterfactual_code_analysis_couterfact_py --> matplotlib_pyplot
    numpy(("numpy"))
    visualization_reddit_simulation_counterfactual_code_analysis_couterfact_py --> numpy
    openai(("openai"))
    visualization_reddit_simulation_counterfactual_code_analysis_couterfact_py --> openai
    scipy_stats(("scipy.stats"))
    visualization_reddit_simulation_counterfactual_code_analysis_couterfact_py --> scipy_stats
    visualization_twitter_simulation_group_polarization_group_polarization_eval_py["visualization/twitter_simulation/group_polarization/group_polarization_eval.py"]
    click visualization_twitter_simulation_group_polarization_group_polarization_eval_py "https://github.com/camel-ai/oasis/blob/main/visualization/twitter_simulation/group_polarization/group_polarization_eval.py" "View source"
    json(("json"))
    visualization_twitter_simulation_group_polarization_group_polarization_eval_py --> json
    logging(("logging"))
    visualization_twitter_simulation_group_polarization_group_polarization_eval_py --> logging
    pandas(("pandas"))
    visualization_twitter_simulation_group_polarization_group_polarization_eval_py --> pandas
    requests(("requests"))
    visualization_twitter_simulation_group_polarization_group_polarization_eval_py --> requests
    tqdm(("tqdm"))
    visualization_twitter_simulation_group_polarization_group_polarization_eval_py --> tqdm
    visualization_twitter_simulation_align_with_real_world_code_graph_py["visualization/twitter_simulation/align_with_real_world/code/graph.py"]
    click visualization_twitter_simulation_align_with_real_world_code_graph_py "https://github.com/camel-ai/oasis/blob/main/visualization/twitter_simulation/align_with_real_world/code/graph.py" "View source"
    sqlite3(("sqlite3"))
    visualization_twitter_simulation_align_with_real_world_code_graph_py --> sqlite3
    matplotlib_pyplot(("matplotlib.pyplot"))
    visualization_twitter_simulation_align_with_real_world_code_graph_py --> matplotlib_pyplot
    networkx(("networkx"))
    visualization_twitter_simulation_align_with_real_world_code_graph_py --> networkx
    pandas(("pandas"))
    visualization_twitter_simulation_align_with_real_world_code_graph_py --> pandas
    graph_utils(("graph_utils"))
    visualization_twitter_simulation_align_with_real_world_code_graph_py --> graph_utils
    pdb(("pdb"))
    visualization_twitter_simulation_align_with_real_world_code_graph_py --> pdb
    pdb(("pdb"))
    visualization_twitter_simulation_align_with_real_world_code_graph_py --> pdb
    pdb(("pdb"))
    visualization_twitter_simulation_align_with_real_world_code_graph_py --> pdb
    pdb(("pdb"))
    visualization_twitter_simulation_align_with_real_world_code_graph_py --> pdb
    visualization_twitter_simulation_align_with_real_world_code_result_ana_mse_py["visualization/twitter_simulation/align_with_real_world/code/result_ana_mse.py"]
    click visualization_twitter_simulation_align_with_real_world_code_result_ana_mse_py "https://github.com/camel-ai/oasis/blob/main/visualization/twitter_simulation/align_with_real_world/code/result_ana_mse.py" "View source"
    os(("os"))
    visualization_twitter_simulation_align_with_real_world_code_result_ana_mse_py --> os
    pickle(("pickle"))
    visualization_twitter_simulation_align_with_real_world_code_result_ana_mse_py --> pickle
    sys(("sys"))
    visualization_twitter_simulation_align_with_real_world_code_result_ana_mse_py --> sys
    pathlib(("pathlib"))
    visualization_twitter_simulation_align_with_real_world_code_result_ana_mse_py --> pathlib
    typing(("typing"))
    visualization_twitter_simulation_align_with_real_world_code_result_ana_mse_py --> typing
    matplotlib_pyplot(("matplotlib.pyplot"))
    visualization_twitter_simulation_align_with_real_world_code_result_ana_mse_py --> matplotlib_pyplot
    numpy(("numpy"))
    visualization_twitter_simulation_align_with_real_world_code_result_ana_mse_py --> numpy
    pandas(("pandas"))
    visualization_twitter_simulation_align_with_real_world_code_result_ana_mse_py --> pandas
    graph(("graph"))
    visualization_twitter_simulation_align_with_real_world_code_result_ana_mse_py --> graph
    tqdm(("tqdm"))
    visualization_twitter_simulation_align_with_real_world_code_result_ana_mse_py --> tqdm
    visualization_twitter_simulation_align_with_real_world_code_result_ana_mean_py["visualization/twitter_simulation/align_with_real_world/code/result_ana_mean.py"]
    click visualization_twitter_simulation_align_with_real_world_code_result_ana_mean_py "https://github.com/camel-ai/oasis/blob/main/visualization/twitter_simulation/align_with_real_world/code/result_ana_mean.py" "View source"
    os(("os"))
    visualization_twitter_simulation_align_with_real_world_code_result_ana_mean_py --> os
    pickle(("pickle"))
    visualization_twitter_simulation_align_with_real_world_code_result_ana_mean_py --> pickle
    pathlib(("pathlib"))
    visualization_twitter_simulation_align_with_real_world_code_result_ana_mean_py --> pathlib
    typing(("typing"))
    visualization_twitter_simulation_align_with_real_world_code_result_ana_mean_py --> typing
    matplotlib_pyplot(("matplotlib.pyplot"))
    visualization_twitter_simulation_align_with_real_world_code_result_ana_mean_py --> matplotlib_pyplot
    numpy(("numpy"))
    visualization_twitter_simulation_align_with_real_world_code_result_ana_mean_py --> numpy
    pandas(("pandas"))
    visualization_twitter_simulation_align_with_real_world_code_result_ana_mean_py --> pandas
    graph(("graph"))
    visualization_twitter_simulation_align_with_real_world_code_result_ana_mean_py --> graph
    tqdm(("tqdm"))
    visualization_twitter_simulation_align_with_real_world_code_result_ana_mean_py --> tqdm
    visualization_twitter_simulation_align_with_real_world_code_graph_utils_py["visualization/twitter_simulation/align_with_real_world/code/graph_utils.py"]
    click visualization_twitter_simulation_align_with_real_world_code_graph_utils_py "https://github.com/camel-ai/oasis/blob/main/visualization/twitter_simulation/align_with_real_world/code/graph_utils.py" "View source"
    matplotlib_pyplot(("matplotlib.pyplot"))
    visualization_twitter_simulation_align_with_real_world_code_graph_utils_py --> matplotlib_pyplot
    networkx(("networkx"))
    visualization_twitter_simulation_align_with_real_world_code_graph_utils_py --> networkx
    visualization_dynamic_follow_network_code_vis_neo4j_reddit_py["visualization/dynamic_follow_network/code/vis_neo4j_reddit.py"]
    click visualization_dynamic_follow_network_code_vis_neo4j_reddit_py "https://github.com/camel-ai/oasis/blob/main/visualization/dynamic_follow_network/code/vis_neo4j_reddit.py" "View source"
    json(("json"))
    visualization_dynamic_follow_network_code_vis_neo4j_reddit_py --> json
    os(("os"))
    visualization_dynamic_follow_network_code_vis_neo4j_reddit_py --> os
    sqlite3(("sqlite3"))
    visualization_dynamic_follow_network_code_vis_neo4j_reddit_py --> sqlite3
    datetime(("datetime"))
    visualization_dynamic_follow_network_code_vis_neo4j_reddit_py --> datetime
    neo4j(("neo4j"))
    visualization_dynamic_follow_network_code_vis_neo4j_reddit_py --> neo4j
    visualization_dynamic_follow_network_code_vis_neo4j_twitter_py["visualization/dynamic_follow_network/code/vis_neo4j_twitter.py"]
    click visualization_dynamic_follow_network_code_vis_neo4j_twitter_py "https://github.com/camel-ai/oasis/blob/main/visualization/dynamic_follow_network/code/vis_neo4j_twitter.py" "View source"
    os(("os"))
    visualization_dynamic_follow_network_code_vis_neo4j_twitter_py --> os
    sqlite3(("sqlite3"))
    visualization_dynamic_follow_network_code_vis_neo4j_twitter_py --> sqlite3
    datetime(("datetime"))
    visualization_dynamic_follow_network_code_vis_neo4j_twitter_py --> datetime
    neo4j(("neo4j"))
    visualization_dynamic_follow_network_code_vis_neo4j_twitter_py --> neo4j
    visualization_reddit_simulation_align_with_human_code_analysis_all_py["visualization/reddit_simulation_align_with_human/code/analysis_all.py"]
    click visualization_reddit_simulation_align_with_human_code_analysis_all_py "https://github.com/camel-ai/oasis/blob/main/visualization/reddit_simulation_align_with_human/code/analysis_all.py" "View source"
    analysis_score(("analysis_score"))
    visualization_reddit_simulation_align_with_human_code_analysis_all_py --> analysis_score
    visualization_reddit_simulation_align_with_human_code___init___py["visualization/reddit_simulation_align_with_human/code/__init__.py"]
    click visualization_reddit_simulation_align_with_human_code___init___py "https://github.com/camel-ai/oasis/blob/main/visualization/reddit_simulation_align_with_human/code/__init__.py" "View source"
    visualization_reddit_simulation_align_with_human_code_analysis_score_py["visualization/reddit_simulation_align_with_human/code/analysis_score.py"]
    click visualization_reddit_simulation_align_with_human_code_analysis_score_py "https://github.com/camel-ai/oasis/blob/main/visualization/reddit_simulation_align_with_human/code/analysis_score.py" "View source"
    json(("json"))
    visualization_reddit_simulation_align_with_human_code_analysis_score_py --> json
    sqlite3(("sqlite3"))
    visualization_reddit_simulation_align_with_human_code_analysis_score_py --> sqlite3
    matplotlib_pyplot(("matplotlib.pyplot"))
    visualization_reddit_simulation_align_with_human_code_analysis_score_py --> matplotlib_pyplot
    numpy(("numpy"))
    visualization_reddit_simulation_align_with_human_code_analysis_score_py --> numpy
    scipy(("scipy"))
    visualization_reddit_simulation_align_with_human_code_analysis_score_py --> scipy
    generator_reddit_user_generate_py["generator/reddit/user_generate.py"]
    click generator_reddit_user_generate_py "https://github.com/camel-ai/oasis/blob/main/generator/reddit/user_generate.py" "View source"
    json(("json"))
    generator_reddit_user_generate_py --> json
    random(("random"))
    generator_reddit_user_generate_py --> random
    concurrent_futures(("concurrent.futures"))
    generator_reddit_user_generate_py --> concurrent_futures
    datetime(("datetime"))
    generator_reddit_user_generate_py --> datetime
    openai(("openai"))
    generator_reddit_user_generate_py --> openai
    generator_twitter_rag_py["generator/twitter/rag.py"]
    click generator_twitter_rag_py "https://github.com/camel-ai/oasis/blob/main/generator/twitter/rag.py" "View source"
    os(("os"))
    generator_twitter_rag_py --> os
    langchain(("langchain"))
    generator_twitter_rag_py --> langchain
    langchain_chroma(("langchain_chroma"))
    generator_twitter_rag_py --> langchain_chroma
    langchain_community_document_loaders_csv_loader(("langchain_community.document_loaders.csv_loader"))
    generator_twitter_rag_py --> langchain_community_document_loaders_csv_loader
    langchain_community_embeddings(("langchain_community.embeddings"))
    generator_twitter_rag_py --> langchain_community_embeddings
    langchain_core_output_parsers(("langchain_core.output_parsers"))
    generator_twitter_rag_py --> langchain_core_output_parsers
    langchain_core_runnables(("langchain_core.runnables"))
    generator_twitter_rag_py --> langchain_core_runnables
    langchain_openai(("langchain_openai"))
    generator_twitter_rag_py --> langchain_openai
    langchain_text_splitters(("langchain_text_splitters"))
    generator_twitter_rag_py --> langchain_text_splitters
    pydantic(("pydantic"))
    generator_twitter_rag_py --> pydantic
    generator_twitter_network_py["generator/twitter/network.py"]
    click generator_twitter_network_py "https://github.com/camel-ai/oasis/blob/main/generator/twitter/network.py" "View source"
    json(("json"))
    generator_twitter_network_py --> json
    random(("random"))
    generator_twitter_network_py --> random
    pandas(("pandas"))
    generator_twitter_network_py --> pandas
    tqdm(("tqdm"))
    generator_twitter_network_py --> tqdm
    generator_twitter___init___py["generator/twitter/__init__.py"]
    click generator_twitter___init___py "https://github.com/camel-ai/oasis/blob/main/generator/twitter/__init__.py" "View source"
    generator_twitter_gen_py["generator/twitter/gen.py"]
    click generator_twitter_gen_py "https://github.com/camel-ai/oasis/blob/main/generator/twitter/gen.py" "View source"
    itertools(("itertools"))
    generator_twitter_gen_py --> itertools
    json(("json"))
    generator_twitter_gen_py --> json
    random(("random"))
    generator_twitter_gen_py --> random
    time(("time"))
    generator_twitter_gen_py --> time
    concurrent_futures(("concurrent.futures"))
    generator_twitter_gen_py --> concurrent_futures
    numpy(("numpy"))
    generator_twitter_gen_py --> numpy
    rag(("rag"))
    generator_twitter_gen_py --> rag
    generator_twitter_ba_py["generator/twitter/ba.py"]
    click generator_twitter_ba_py "https://github.com/camel-ai/oasis/blob/main/generator/twitter/ba.py" "View source"
    random(("random"))
    generator_twitter_ba_py --> random
    pandas(("pandas"))
    generator_twitter_ba_py --> pandas
    db_sqlite[(SQLite)]
```

## Discovered Technologies

- **Frameworks**: None detected
- **Databases**: SQLite
- **APIs**: REST Client

## External Dependencies

itertools, requests, time, pathlib, heapq, enum, langchain_core, clock, numpy, uuid, langchain_community, math, dataclasses, scipy, pickle, agent_graph, warnings, user, process_recsys_posts, matplotlib, subprocess, camel, langchain_openai, graph_utils, analysis_score, pydantic, rag, langchain_chroma, tqdm, os, igraph, channel, sentence_transformers, asyncio, pandas, pdb, abc, ast, yaml, oasis, networkx, langchain, graph, datetime, platform, openai, sklearn, agents_generator, aiohttp, agent, concurrent, transformers, tempfile, random, torch, sys, pytest, typing, json, inspect, threading, neo4j, logging, colorama, string, __future__, utils, re, argparse, langchain_text_splitters, sqlite3
