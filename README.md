#

## Software development for web and mobile. Session 12

https://slides.com/pepegar/sdwm-12/live

#

## Plan for today

* Why we need templating?
* Understand HTML templating
* Jinja + Flask

#

## Why we need HTML templating?

## The problem

Imagine we're trying to create a web application with, say, five
different screens.  Using the approach we've been following until now,
we would need to repeat some common code in all screens.

## Example 1

See /example1 project.

**What should we do for creating the products page?**

#

## Introducing templating

HTML templating is a technique we will use to make writing HTML more
pleasant, easy, and less repetitive.

## Jinja templates

Jinja is a framework for HTML templating that is already integrated
with Flask.  With Jinja we can:

- Using variables
- use conditionals
- use loops
- inherit other templates

## Jinja syntax

We write Jinja templates in plain HTML documents.  Apart of the normal
HTML syntax, we get two new _tags_.

- `{{ }}` for expressions.
- `{% %}` for statements. (control flow)

## Using variables in templates

We can use Jinja to write HTML templates that have parametrized
variables:

```html
<html>
  <head>
    <title>Hello {{name}}!</title>
  </head>
  <body>
    <h1>Hello {{name}}!</h1>
  </body>
</html>
```

## Rendering templates from Flask

There is a `render_template` function that we can impoort from `flask`
to render templates.  Something important to take into consideration
is that flask is going to look for templates in the `templates`
directory.

## Rendering templates from Flask

```python
@app.route("/hello/<name>")
def hello(name):
    return render_template("hello.html", name=name)
```

## Example 2

see /example2

## conditionals

something very common in templating -and programming in general- is
using conditionals.  We can use conditionals in templates to render
different things depending on different conditions.

## loops



## inheriting other templates

http://jinja.pocoo.org/docs/2.10/templates/#template-inheritance

#

## Exercises

## White belt

## Blue belt

## Black belt
