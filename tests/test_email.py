import pytest
import pickle
from zotero_arxiv_daily.protocol import Paper
from zotero_arxiv_daily.construct_email import render_email
from zotero_arxiv_daily.utils import send_email
@pytest.fixture
def papers() -> list[Paper]:
    with open("tests/paper_full.pkl", "rb") as f:
        paper = pickle.load(f)
    return [paper]*10

def test_render_email(papers:list[Paper]):
    email_content = render_email(papers)
    assert email_content is not None

def test_send_email(config,papers:list[Paper]):
    send_email(config, render_email(papers))