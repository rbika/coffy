<h1>Coffy Time!</h1>

<form action="/add" method="get">
  <input type="text" name="name"/>
  <input type="submit" value="Add name">
</form>

<form action="/" method="get">
  %for p in names:
    <input id="id_{{ p }}" type="checkbox" name="names" value="{{ p }}">
    <label for="id_{{ p }}">{{ p }}</label><br/>
  %end
  <br><input type="submit" value="Run Coffy">

  %if result:
    <b>{{ result }}</b>
  %end
</form>
