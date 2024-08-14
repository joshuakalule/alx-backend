# Flask Babel

Add internalization support to flask application.

## Procedure

1. Extract text to be translated and add them to `.pot` file

    `$ pybabel extract -F babel.cfg -o messages.pot dir`

    *-F*: config files containing regex for files to be checked\
    *-o*: output file\
    *dir*: directory within which to check for files

2. Create edittable files(.po) for each language

    `$ pybabel init -i messages.pot -d translations -l en`

    *-i*: .pot file to use\
    *-d*: directory to put the files\
    *-l*: language

3. Add the translations in the files `.po` in the created translations folder

4. Compile the files (`.po` -> `.mo`)

   `$ pybabel compile -d translations`

   *-d*: folder with the `.po` files

*PS:* If the strings change, create a new `.pot` file and run below to merge the changes
`$ pybabel update -i messages.pot -d translations`

## Common errors

`jinja2.ext has no attribute autoescape`
[Solution]: pip3 install 'jinja<3.1.0'
