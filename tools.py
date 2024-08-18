from crewai_tools import SerperDevTool , WebsiteSearchTool

# os.environ["Gemini_API_KEY"] = "AIzaSyCfMPceVOPwQ5j3Ke9O7SaaOUSIveBrgis"
# os.environ["SERPER_API_KEY"] = "757f470508a8904d687632677534633ea490fe68b7a528cc3fb3b94cf05b28ee"
#tools.py



searchTool = SerperDevTool()

WebsiteSearchTool = WebsiteSearchTool(
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
        ),
          # Directly provide your Google API key here
    )
)



