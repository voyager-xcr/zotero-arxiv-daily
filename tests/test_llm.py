import pytest
import pickle
from openai import OpenAI
from zotero_arxiv_daily.protocol import Paper
@pytest.fixture
def paper() -> Paper:
    with open("tests/paper.pkl", "rb") as f:
        paper = pickle.load(f)
    return paper

def test_tldr(config,paper:Paper):
    openai_client = OpenAI(api_key=config.llm.api.key, base_url=config.llm.api.base_url)
    paper.generate_tldr(openai_client, config.llm)
    assert paper.tldr is not None

def test_affiliations(config,paper:Paper):
    openai_client = OpenAI(api_key=config.llm.api.key, base_url=config.llm.api.base_url)
    paper.generate_affiliations(openai_client, config.llm)
    assert paper.affiliations is not None