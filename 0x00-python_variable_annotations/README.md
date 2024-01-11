<h3>Variable Annotations</h3>
<ul>
    <li>
        Type annotations in Python 3
    </li>
    <li>
        How you can use type annotations to specify function signatures and variable types
    </li>
    <li>
        Duck typing
    </li>
    <li>
        How to validate your code with mypy
    </li>
</ul>

<div class="gap formatted-content">
    <p>Python is a dynamically-typed language. That means that variable types are dynamically set at run-time, upon assignment of a value to a variable.</p>

<p>For example, in</p>

<pre><code class="python">def fn(a, b):
    return a + b
</code></pre>

<p>The types of <code>a</code> and <code>b</code> are not known at build-time, only when <code>a</code> and <code>b</code> are assigned values at run-time.</p>

<p>Hence, calling</p>

<pre><code class="python">fn(&quot;a&quot;, 1)
</code></pre>

<p>somewhere in your code will not raise an exception until the code is actually executed and the function is called:</p>

<pre><code>&gt;&gt;&gt; fn(&quot;a&quot;, 1)
Traceback (most recent call last):
  File &quot;&lt;stdin&gt;&quot;, line 1, in &lt;module&gt;
TypeError: can only concatenate str (not &quot;int&quot;) to str
</code></pre>

<p>In Python 3, type annotations do not change this. Python is still a dynamically-typed language. Type annotations serve the following purpose:</p>

<ul>
<li>Code documentation: thanks to them, a developer reading type-annotated code (his own or someone else&rsquo;s) will know exactly what type each variables is supposed to be. This helps reduce bugs and exceptions and accelerate the development cycle.</li>
<li>Linting and validation: code editors and continuous integration (CI) pipelines can be configured to automatically validate type-annotated code at build-time and catch bugs before they make it to production.</li>
</ul>

</div>