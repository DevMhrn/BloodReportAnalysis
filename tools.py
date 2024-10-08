from crewai_tools import SerperDevTool , WebsiteSearchTool

searchTool = SerperDevTool()

websiteSearchTool = WebsiteSearchTool(
    config=dict(
        llm=dict(
            provider="google",
            config=dict(
                model="gemini-pro",
                temperature=0.7,
                api_key="AIzaSyCfMPceVOPwQ5j3Ke9O7SaaOUSIveBrgis"
            ),
        ),
        embedder=dict(
            provider="google",
            config=dict(
                model="models/embedding-001",
                task_type="retrieval_document",
            ),
        )
    )
)



