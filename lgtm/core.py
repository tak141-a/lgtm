import click

@click.command()
def cli():
    """LGTM画像生成ツール エントリポイント"""
    lgtm()
    click.echo('lgtm')  # 動作確認用

def lgtm():
    # ここにロジックを追加していく
    pass
