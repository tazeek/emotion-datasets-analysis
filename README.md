# Data Analysis

Each file will have it's own analysis code. It consists of the following:

### Attributes

- Store data for analysis purposes.
- Data format is the one **BEFORE** visualization.
- There can be as many attributes as possible.

### Methods

- Navigating through the data schema.
- One method can only do **ONE THING**.
- Keeping code short and simple is the key.

### Others

- File must not contain **visualization code**.
- Visualization is only in **Jupyter Notebooks**.
- Documentation/Explanation is in either individual README or Jupyter Notebooks.

### How it works

1. Create the object
-- Optional: Some may require the partitioned part to be passed in

2. Analysis is done on object creation itself

3. Fetch the analyzed parts
-- This is the raw data of the analysis
-- No preprocessing is done for visualization