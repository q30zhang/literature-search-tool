# Literature Search Tool

This project is a designed web UI based on [Quarto](https://quarto.org) that helps organize and look up literatures for academic studies. It uses [BibTeX](https://www.bibtex.org) source files (`*.bib`) to render the UI, making it easy to use and align to academic writing. 

## Installation and Initialization

1. Install [Quarto](https://quarto.org) and choose your dev tool.
2. Fork/clone the repository and set it up as a github page (deploy from `/docs`).
3. Replace the `*.bib` source files in `/data_bibtex` and rebuild:

    ```
    cd <path-to-project>
    quarto render
    ```

4. Host locally by executing `quarto preview` (for under development), or host it statically at `http://127.0.0.1:8000`:

    ```
    cd <path-to-project>/docs
    python3 -m http.server 8000
    ```

    Alternatively, push to GitHub and host it through [GitHub Pages](https://docs.github.com/en/pages). In the settings of the repo, select "Page" and select **Deploy from a branch**, and select the `main` branch and `/docs` directory.

5. If you have local PDF files for the corresponding literatures, you can host a local server to enable quick viewing from the UI:

<ol><ol type="a">
<li><p>Host a local html server in the directory of your PDF files:</p>
<pre><code>cd &lt;your_pdf_directory&gt;
python3 -m http.server 4000
</code></pre>
<p>You can choose the port, but you need to update it in <code>_quarto.yml</code> if you do so.</p>
</li>
<li><p>Organize the PDF files for the papers in directories with the same name as the corresponding <code>.bib</code> files, and rename the PDF files as the paper's title, where all <code>white space</code> are replaced with <code>_</code>.</p>
<p>For example, if you have a paper in <code>data_bibtex/part_A.bib</code>, whose title is "My First Cited Paper", then this PDF file should be placed in <code>&lt;your_pdf_directory&gt;/part_A/My_First_Cited_Paper.pdf</code>.</p>
</li>
</ol>
Then the <b>PDF</b> links should direct to the local PDF files!
</ol>

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