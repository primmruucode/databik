import pandas as pd


business_data = pd.read_csv("dbfs/my-data/data.csv")

class GreatDatabricksPipeline:
  """ A Data pipeline that will run on databricks :)
  """
  def __init__(self, data: pd.DataFrame) -> None:
    self.data = data

  def run(self) -> None:
    """ Run Datatabricks pipeline method.
    """
    pass


pipeline = GreatDatabricksPipeline(data = business_data)
pipeline.run()
