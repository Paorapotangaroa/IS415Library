class Statistics():

    def __init__(self, dataframe) -> None:
        # import libraries and set the dataframe attribute
        self.df = dataframe

    def describeData(self, columns=[]):
        import pandas as pd
        # If they choose not to pass columns then return a description of all columns
        if (columns == []):
            return self.df.describe()
        else:
            # If they choose to pass columns only describe the relevant columns of the dataframe
            return self.df[columns].describe()

    def getDataTypes(self, columns=[]):
        import pandas as pd
        # If they choose not to pass columns then return the types of the entire dataframe
        if (columns == []):
            return self.df.dtypes
        else:
            # Return the specific types for relevant columns if specified
            return self.df[columns].dtypes

    def getDataCountsByColumn(self, columns=[]):
        import pandas as pd
        if (columns == []):
            return self.df.count()
        else:
            return self.df[columns].count()

    def getUniqueDataCountsByColumn(self, columns=[]):
        import pandas as pd
        if (columns == []):
            return self.df.nunique()
        else:
            return self.df[columns].nunique()

    def getUniqueDataByColumn(self, column: str):
        import pandas as pd
        return self.df[column].unique()

    def sumMissingValues(self, columns=[]):
        import pandas as pd
        if (columns == []):
            return self.df.isna().sum()
        else:
            return self.df[columns].isna().sum()

    def getDataShape(self):
        import pandas as pd
        return self.df.shape

    def getMean(self, columns=[]):
        import pandas as pd
        import numpy as np

        # If we have no columns specified: It doesn't make sense to return the mean of non-numeric.
        # Therefore we only select numeric types and return them
        if (columns == []):
            return self.df.select_dtypes(include=np.number).mean()
        else:
            # If they specified a column/columns: Return the mean for those columns. Will throw an error if user
            # specifies a non-numeric datatype
            return self.df[columns].mean()
