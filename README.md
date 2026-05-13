# Literature Search Tool

This project is a designed web UI based on Quarto that helps organize and look up literatures for academic studies. It uses [BibTeX](https://www.bibtex.org) source files (`*.bib`) to render the UI, making it easy to use and align to academic writing. 

## Installation and Initialization

1. Install [Quarto](https://quarto.org) and choose your dev tool.
2. Fork/clone the repository and set it up as a github page (deploy from `/docs`).
3. Replace the `*.bib` source files in `/data_bibtex` and rebuild from fresh:

    ```
    quarto clean
    quarto render
    ```

4. If you have local PDF files for the corresponding literatures, you can host a local server to enable quick viewing from the UI:

    a.  Host a local html server in the directory of your PDF files:

            cd <your_pdf_directory>
            python3 -m http.server 4000
        You can choose the port, but you need to update it in `_quarto.yml` if you do so.

    b.  Organize the PDF files for the papers in directories with the same name as the corresponding `.bib` files, and rename the PDF files as the paper's title, where all `white space` are replaced with `_`.
    
        <!-- -->
        For example, if you have a paper in `data_bibtex/part_A.bib`, whose title is "My First Cited Paper", then this PDF file should be placed in `<your_pdf_directory>/part_A/My_First_Cited_Paper.pdf`.</p>

    Then the **PDF** links should direct to the local PDF files!

## Organization

It is suggested that you organize your literatures BibTeX as:

```
literature_search_tool/
├── data_bibtex/
│   ├── category_A.bib
│   ├── category_B.bib
│   └── ...
└── ...
```

Your local paper folder:

```
<paper_pdf_directory>
├── category_A/
│   ├── First_Paper_Title_of_Category_A.pdf
│   ├── Second_Paper_Title_of_Category_A.pdf
│   └── ...
└── category_B/
    ├── First_Paper_Title_of_Category_B.pdf
    ├── Second_Paper_Title_of_Category_B.pdf
    └── ...
```

## Example UI site

This is the [literature collection for my master's thesis](https://q30zhang.github.io/literature-search-tool/literatures_list.html).