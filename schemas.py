from typing import List, Dict, Any
from pydantic import BaseModel, Field

class StartupAnalysis(BaseModel):
    verdict: str

    novelty: int
    market_potential: int
    competition_risk: int
    monetization_potential: int
    technical_difficulty: int

    vc_likes: List[str]
    vc_concerns: List[str]

    risks: List[str]
    mvp_features: List[str]

    similar_startups: List[str]

    summary: str