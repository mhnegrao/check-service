<script>
  import Grid from "./../components/Grid.svelte";
  import Header from "./../components/Header.svelte";
</script>

<section>
  <Header titulo="Check Service" descricao="Verificador de Serviços Windows" />

  <label for="txtService">Digite o nome do serviço a ser pesquisa</label>
  <input type="text" name="txtService" id="txtService" />
  <button class="btn btn-primary">Pesquisar</button>

  <Grid />
  
</section>

<style>
</style>
