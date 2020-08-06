<script lang="ts">
  import axios from 'axios';
  import { writable } from 'svelte/store';
  export let userid: string;
  export let pw: string;
  export let click;
  export let error;

</script>

<h1>Welcome to dtan's Tic tac toe!</h1><br>
<p>{error.message}</p>
<label>ID: </label>
<input type="text" bind:value={userid}><br>
<label>PW: </label>
<input type="password" bind:value={pw}><br>
<button class="signin" on:click={click}>Sign in</button>