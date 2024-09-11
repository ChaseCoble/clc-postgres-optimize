Chase Coble's Portfolio API
Version 1.0: Functionality is primarily the maintenance of content for the NextJS frontend of the portfolio. Utilizing SQLAlchemy, FastAPI, and Alembic to maintain and update a Postgressql database. Certain behaviours currently handled by the API will be migrated over to Postgressql trigger functions.

Current content types are:
    
    Portfolio : Portfolio items, projects
    
    Articles : Written articles on various academic or social subjects.
    
    Skills : A quantified measure of career relevant skills
    
    Education: Merits of various kinds from educational activities. Primarily degree and certifications
    
    Career: Work experience relevant to my current roles.

    Links: Various online presences such as Github, Linkedin or similar.

    Singleton: A wrapper column for objects that should only have one copy.

    User: Authentication control table for only content modifications

    Updateables: Generic category for rarely updated content such as images, contact information, and other information

    Machine Learning Columns:
        Regression: Datasets and calculations specifically for providing already processed data for machine learning demonstrations utilizing regression. IN PROGRESS
        KNeighbors: Datasets and calculations specifically for providing already processed data for machine learning demonstrations utilizing regression. Experimentally considering a mathematical model to model most KNeighbor relationships to a 3D graph. Can be used with KMEANs as well
        IN PROGRESS