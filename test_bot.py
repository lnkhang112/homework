from bot import Bot

def test_bot_runs():
    try:
        Bot()
        assert True
    except Exception as e:
        assert False, f"Bot failed with error: {e}"