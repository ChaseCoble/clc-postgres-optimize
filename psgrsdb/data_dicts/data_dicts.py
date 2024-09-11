from ..schemas import articles, career, education, kNeighbors, links, portfolio, regression, skills
from ..models import *

model_dict = {
    "gen": {
        "portfolio": {
            "model": PortfolioItems,
            "schema": {
                "create": portfolio.PortfolioCreate,
                "get" : portfolio.PortfolioGet,
                "update": portfolio.PortfolioUpdate,
                "delete": portfolio.PortfolioDelete
            }
        },
        "articles": {
            "model": Articles,
            "schema": {
                "create" : articles.ArticlesCreate,
                "get": articles.ArticlesGet,
                "update": articles.ArticlesUpdate,
                "delete": articles.ArticlesDelete
            }
        },
        "career": {
            "model": Career,
            "schema": {
                "create": career.CareerCreate,
                "get": career.CareerGet,
                "update": career.CareerUpdate,
                "delete": career.CareerDelete
            }
        },
        "education": {
            "model": Education,
            "schema": {
                "create": education.EducationCreate,
                "get": education.EducationGet,
                "update": education.EducationUpdate,
                "delete": education.EducationDelete
            }
        },
        "links": {
            "model": Links,
            "schema": {
                "create" : links.LinksCreate,
                "get": links.LinksGet,
                "update": links.LinksUpdate,
                "delete": links.LinksDelete
                }
            },
        "skills":{
            "model": Skills,
            "schema": {
                "create": skills.SkillCreate,
                "get": skills.SkillGet,
                "update": skills.SkillUpdate,
                "delete": skills.SkillDelete
            }
        }    
    },
    "ml": {
        "regression": {
            "model": Regression,
            "schema": {
                "create" : regression.RegressionCreate,
                "get": regression.RegressionGet,
                "update": regression.RegressionUpdate,
                "delete": regression.RegressionDelete
                }
            },
        "k_neighbors": {
            "model": KNeighbors,
            "schema": {
                "create" : kNeighbors.KNeighborsCreate,
                "get": kNeighbors.KNeighborsGet,
                "update": kNeighbors.KNeighborsUpdate,
                "delete": kNeighbors.KNeighborsDelete
                }
            }
        }
    }


content_dict = {
    "content": {
        "gen": {
            "portfolio": [],
            "articles": [],
            "links": [],
            "education": [],
            "career": [],
            "updateables": [],
            "skills": []
        },
        "ml": {
            "regression": [],
            "kNeighbors": []
        }
    }
}

update_dict = {
        "gen" : Singleton.update,
        "ml" : Singleton.ml_update
}