import pytest
from datetime import date
from dB_3BM_Project import dqte_du_jour


def test_dqte_du_jour_format():
    today_str = dqte_du_jour()
    assert isinstance(today_str, str)
    assert today_str == date.today().isoformat()
