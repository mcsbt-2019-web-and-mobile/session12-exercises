#

## Software development for web and mobile. Session 12

#

## Plan for today

* Why do we need templating?
* Understand HTML templating
* Jinja + Flask

#

## Why do we need HTML templating?

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

#

## conditionals

something very common in templating -and programming in general- is
using conditionals.  We can use conditionals in templates to render
different things depending on different conditions.

## conditionals

Since conditionals are statements (they don't produce a value), we'll
use the `{% %}` syntax for them:

``` html
<html>
  <head>
  </head>
  <body>
    {% if user.logged %}
      <h1>Hello {{user.name}}</h1>
    {% else %}
	  <h1>Hello, normal person. <button>login?</button></h1>
    {% endif %}
  </body>
</html>
```

## Example 3

See /example3

#

## loops

We can perform iterative tasks inside templates as well!  We just need
to use a for loop :)

## loops

``` html
<html>
  <head>
  </head>
  <body>
    {% for item in items %}
      <article id="article-{{item.id}}">
	    <img src="{{item.img}}"/>
	    <div class="name">{{item.name}}</div>
		<div class="price">{{item.price}}</div>
        <div class="description">{{item.description}}</div>
		<button class="buy">add to basket</div>
	  </article>
    {% endfor %}
  </body>
</html>
```

## Example 4

see /example4

#

## Template inheritance

Inheritance is one of the most interesting features of Jinja.  When
using inheritance, we'll create **parent** templates that will be extended
by **child** templates.  **Child** templates will be able to override
parent's blocks if needed.

## Template inheritance

When using inheritance, we will need to to add to the parent template
the **blocks** that children will be able to override.  Let's see an
example:

``` html
<html>
  <head>
    <title>{% block title %}{% endblock %}</title>
  </head>
  <body>
    {% block body %}
	{% endblock %}
  </body>
</html>
```

## Template inheritance

Then later, when creating the **child** template, we need to tell
jinja which template we're extending and what blocks we're overriding:

``` html
{% extends "base.html" %}
{% block title %}this is my title!{% endblock %}
{% block body %}<h1>this is generated using template inheritance!</h1>{% endblock %}
```

#

## Exercises

Remember `/example1`?  let's solve it by using template inheritance!

We'll need to create different pages for all elements in the menu.

#

## Bootstrap

Bootstrap is a frontend component library.  It contains styles and JS
for a lot of different cases, and we can start using it with just a
few lines of code:

https://getbootstrap.com/

## Example 6

Integrating bootstrap in our simple web page.

#

## Homework

Create a blogging system.  It should:

- have a page for writing new posts
- _blue_: have a page for displaying all posts titles
- _blue_: have a page for displaying a specific post
- _blue_: make all different screens use template inheritance
- _black_: use Bootstrap for UI components
