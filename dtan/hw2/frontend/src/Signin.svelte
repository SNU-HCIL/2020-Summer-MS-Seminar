<script lang="ts">
  export let userid: string;
  export let pw: string;
  export let click: svelte.JSX.EventHandler<MouseEvent,HTMLButtonElement>;
</script>

<h1>Welcome to dtan's Tic tac toe!</h1><br>
<label>ID: </label>
<input type="text" bind:value={userid}><br>
<label>PW: </label>
<input type="password" bind:value={pw}><br>
<button class="signin" on:click={click}>Sign in</button>