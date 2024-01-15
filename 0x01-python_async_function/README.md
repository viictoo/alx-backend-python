<h2>Learning Objectives</h2>


<pre><code>
pycodestyle style (version 2.5.x) || type-annotated
</code></pre>

<ul>
<li><code>async</code> and <code>await</code> syntax</li>
<li>How to execute an async program with <code>asyncio</code></li>
<li>How to run concurrent coroutines</li>
<li>How to create <code>asyncio</code> tasks</li>
<li>How to use the <code>random</code> module</li>
</ul>

<p>

    Asynchronous IO (async IO): a language-agnostic paradigm (model) that has implementations across a host of programming languages

    async/await: two new Python keywords that are used to define coroutines

    async: A style of concurrent programming in which tasks release the CPU during waiting periods so that other tasks can use it

    implementations: 
    <ul>
        <li>Callback functions</li>
        <li>Generator Functions</li>
        <li>Async/Await</li>
        <li>Greenlets</li>
    </ul>

    asyncio | gevent

    <code>import asyncio


loop = asyncio.get_event_loop()

async def hello():
    print('hello')
    await asyncio.sleep(3)
    print('world')

if __name__ == '__main__':
    loop.run_until_complete(hello())
    </code>

    asyncio: the Python package that provides a foundation and API for running and managing coroutines

</p>