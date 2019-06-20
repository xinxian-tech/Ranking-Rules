# Ranking Rules
This script will rank the contribution of team member's contribution over a task according to the members' public voting. Ranking and weights will be generated. The algorithm is based on analytic hierarchy process (AHP), see [Wikipedia](https://en.wikipedia.org/wiki/Analytic_hierarchy_process) for the details.



### Usage
The ranking process is divided into voting and ranking. `generate_tables.py` will generate a voting table (.csv file) according to the related member's names. When all the members filled the tables, `rank.py` will give the ranking according to result in the tables.

##### Generate Tables

``` bash
python3 generate_tables.py [-h] --names NAMES [--output_path OUTPUT_PATH]
```

##### Fill the Tables
Theoretically, each member is responsible for filling one voting table. In the table, there is a matrix with all member names as column and row names. The matrix is initialized as all-1 matrix. Suppose **the element in i th row and j th column is a_ij**, the value of it should be filled with respect to the following creteria.

| value of a_ij |                       meaning                        |
| :-----------: | :--------------------------------------------------: |
|       1       |          member i and j contribute equally           |
|       3       |   member i contribute slightly more than member j    |
|       5       |   member i contribute strongly more than member j    |
|       7       | member i contribute very strongly more than member j |
|       9       |   member i contribute extremely more than member j   |

Note that the following relationship holds.

``` 
a_ii = 0
a_ij = 1 / a_ji
```

The table should be saved as .csv file.

##### Generate Ranking

After gathering all members' submission of voting tables into a directory, the result can be fetched by running the following command.

``` bash
python3 rank.py [-h] [--input_dir INPUT_DIR]
```



### Example

Here is a brief example of using this script.

##### Generate Tables

``` bash
$ python3 generate_tables.py --names "Donald Trump,Влади́мир Влади́мирович Пу́тин,习近平,Theresa Mary May,Emmanuel Jean-Michel Frédéric Macron"
Generation complete. See the output files at ./vote_table.csv
After filling the tables, run rank.py
```

##### Fill the Voting Table

![Sample Filling](https://i.imgur.com/P2jtx54.png)

##### Get the Ranking result

``` bash
$ python3 rank.py
______________________________________________________________________
   ranking              weight                  name
         1             0.41316     Влади́мир Влади́мирович Пу́тин
         2             0.23527              Donald Trump
         3             0.21423            Theresa Mary May
         4             0.08684                  习近平
         5             0.05050  Emmanuel Jean-Michel Frédéric Macron
CI: 0.07077638131664488
----------------------------------------------------------------------
```

