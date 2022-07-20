<script>
  export let titulo = "Resultado da Pesquisa";
  export let lista = [{}];
</script>

<h3>{titulo}</h3>
<br />
<table class="table">
  <thead>
    <throw />
  </thead>
  <tbody>
    <trow>
      {#each lista as item}
        <tcol>{item}</tcol>
      {/each}
    </trow>
  </tbody>
</table>

<style>
</style>
