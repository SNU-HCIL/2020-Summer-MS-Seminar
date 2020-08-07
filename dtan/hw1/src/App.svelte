<script lang="ts">
	import Game from './Game.svelte';
</script>

<svelte:head>
	<title>dtan's Tic Tac Toe</title>
</svelte:head>

<main>
	<Game />
</main>

<style>
	main {
		text-align: center;
		padding: 1em;
		max-width: 240px;
		font: 14px "Century Gothic", Futura, sans-serif;
		margin: 20px;
	}

	@media (min-width: 640px) {
		main {
			max-width: none;
		}
	}
</style>