<script lang="ts">

	import Board from './Board.svelte'
	import Log from './Log.svelte'
	import Login from './Login.svelte'
	import Record from './Record.svelte'
	import { onMount } from 'svelte'
	import { loginSuccessStore, idStore } from './stores'

	let loginSuccess : boolean;
	let id : string;
	onMount(() => {
		loginSuccessStore.subscribe(v => {		// register loginSuceess Variable
			loginSuccess = v;
		})
		idStore.subscribe(v => {  				// register id Variable
			id = v;
		})
		idStore.set("");
	})


</script>

<main>
	<h1>Tic Tac Toe</h1>
	{#if loginSuccess}     <!-- After Login-->
	<div id="main-view">
		<Board/>
		<Record/>
		<!-- <Log/> -->    <!-- Logging disabled in hw2 -->
	</div>
	{:else}				  <!-- After Login-->
		<Login/>	
	{/if}

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

	#main-view {
		display: inline-flex;
	}
</style>