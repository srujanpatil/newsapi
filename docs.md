<h1>Guardian News API Docs</h1>
<h2>Endpoints</h2>
<div>
    <ul>
        <li>/list</li>
        <li>/search</li>
        <li>/article/id</li>
        <br>
    </ul>
</div>
<hr>
<div>
    <h3>/list?start=0</h3>
    <p>This endpoint returns a list of available articles</p>
    <h4>Available Methods</h4>
    <ul>
        <li>GET</li>
    </ul>
    <h5>Query parameters</h5>
    <ul>
        <li>start (int): Start of the page</li>
    </ul>
</div>
<hr>
<div>
    <h3>/search?query=keyword&start=0</h3>
    <p>This endpoint returns a list of available articles with searched keyword</p>
    <h4>Available Methods</h4>
    <ul>
        <li>GET</li>
    </ul>
    <h5>Query parameters</h5>
    <ul>
        <li>query (str): Search keyword</li>
        <li>start (int): Start of the page</li>
    </ul>
</div>
<hr>
<div>
    <h3>/article/id</h3>
    <p>This endpoint returns details about the specified articles</p>
    <h4>Available Methods</h4>
    <ul>
        <li>GET</li>
    </ul>
</div>
