<script lang="ts">

	import Board from './Board.svelte'


</script>

<main>
	<h1>Tic Tac Toe</h1>
	<Board/>
</main>

<style type="text/scss"> 
	main {
		text-align: center;
		padding: 1em;
		max-width: 240px;
		margin: 0 auto;
	}

	h1 {
		color: #79a7e8;
		text-transform: uppercase;
		font-size: 3em;
		font-weight: 100;
	}

	@media (min-width: 640px) {
		main {
			max-width: none;
		}
	}
</style>