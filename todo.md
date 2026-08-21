# Missions: SIMPLE PDF MERGER Implementation

Read following mission carefully, perform one by one.
After finishing the job, update its state like marking completion.

## Mission 1: Start - COMPLETED

Your mission is to make a simple pdf merger.
It works on most os including windows, ubuntu and mac os.
I prefer python based using uv framework.
It works like this.

```bash
# current folder(ex 'abc')  has following 1.pdf, 2.pdf, 3.pdf. 
# after running following command
pdf-merge .
# then generate abc.pdf merging 1.pdf 2.pdf & 3.pdf.  
```

## Mission 2: `uv tool install .` - COMPLETED

- 'uv tool install [package folder]` is very useful for this kind of tool installation.
- Add this installation way to README.md
- Make it this default installation way in the document.

## Mission 3: Page Size Normalized Merge - COMPLETED

- I found that when pdfs page size are various, merged-pdf seems ugly.
- We need a feature to normalize page size to A4 or anything else.
- Multi page sized pdfs are located in `test/_backup` folder.
- Also trying merging for `test/_backup` makes strange messages.
- Trace why this happens and resolve it if needed.

## Mission 4: GitHub Installation - COMPLETED

- Add installation from GitHub using `uv tool install git+https://...`
- Update README with git+https installation instructions.
