I’m glad you found this repository and hope it helps you achieve your goals.

This repository is designed to assist you in uncovering a fund portfolio. To use it, you'll need to provide simple files with the columns labeled "Ativos," "Financeiro," and "%PI."

**** IMPORTANT NOTES ****

First, ensure that you include all involved portfolios in the process. For example, if you are analyzing a portfolio that invests in other portfolios, you need to place both portfolio files in the "Carteiras" folder:

<img width="445" alt="Screenshot 2024-08-19 at 1 45 13 am" src="https://github.com/user-attachments/assets/640a4892-75b6-47f1-8322-bc4497549518">


It's important to list the names of the files in "explodir carteiras.xlsx":

<img width="141" alt="Screenshot 2024-08-19 at 1 45 31 am" src="https://github.com/user-attachments/assets/b523468e-0d9c-432a-ae44-fb06ba4b8d49">


The function provides two types of output: Excel export and variable output.

Excel Export: Import or incorporate this function into your code and set the parameter externo to "exportar". This will generate an Excel file with three sheets:
"all_assets": Contains assets and fund lines included in the portfolio.
"without_funds": Lists assets without fund lines but indicates their source.
"agrouped": Shows the entire portfolio grouped together.

Variable Output: If you choose the variable output, set externo to "noexportar". This will also produce an Excel file with the same three sheets as described above.

Enjoy it!!
