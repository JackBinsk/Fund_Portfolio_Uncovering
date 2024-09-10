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

Lets check the xlsx out.

<img width="151" alt="Screenshot 2024-09-10 at 9 20 57 AM" src="https://github.com/user-attachments/assets/5ff5356e-cc57-4fc0-9c23-e3d778d2f978">

If you didnt have any problem running the program, your first look on the progam should like this image below:

<img width="550" alt="Screenshot 2024-09-10 at 9 35 29 AM" src="https://github.com/user-attachments/assets/7a37df7c-4d38-4dc7-beb4-02d0e3ea8eb9">

Lets understand first the all_assets sheet. As you can see in the above image, there are some rows with check = 1 and it means that this asset is fund which was uncovered.

Once the asset has a check 1 (or it had been processed), it must shows up in the fund's portfolio like this:

<img width="709" alt="Screenshot 2024-09-10 at 9 56 06 AM" src="https://github.com/user-attachments/assets/d7242fb6-fa86-41be-8d79-fb50112618e4">

As you can see in "Caminho", you can track the way made by the asset. The "ativo 20" came from the fundo 1, and for it's time came from the master fund.

Lastly, everytime when a asset showed up in the portfolio from different funds, we can notice that the fundo 3 showed up 2 time during the uncovering have made the way:

master - fundo 1 - fundo 2 - fundo 3

and the another one:

master - fundo 2 - fundo 3

both, obvisouly, came from master fund, and then they separete at the segund branch.

<img width="694" alt="Screenshot 2024-09-10 at 10 03 22 AM" src="https://github.com/user-attachments/assets/e05450ea-43e8-4b0f-9bad-cfe411fa9978">

Enjoy it!!
