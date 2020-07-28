<script lang="ts">
	import Board from './Board.svelte'
	import {BoardManager} from './BoardManager'
	import {fade, fly} from'svelte/transition'
	const gameHistory = BoardManager.gameHistory
	const gameStatus = BoardManager.gameStatus
</script>

<main>
	<div class="tic-tac-toe">
		<div class="board">
			<Board/>
		</div>
	</div>
	<div class="game-log">
		<div class="status">
			{#if $gameStatus == "Win"}
				<b>Winner: {$gameHistory.currentState().turnOfTheFirst ? 'O': 'X'}</b>
			{:else if $gameStatus == "Draw"}
				<b>Draw</b>
			{:else}
				Next Player: {$gameHistory.currentState().turnOfTheFirst ? 'O': 'X'}
			{/if}

		</div>
		<div class="actions">
			{#if $gameHistory.canUndo()}
				<button on:click={gameHistory.undo}>Undo</button>
			{:else}
				<button disabled>Undo</button>
			{/if}
			{#if $gameHistory.canRedo()}
				<button on:click={gameHistory.redo}>Redo</button>
			{:else}
				<button disabled>Redo</button>
			{/if}
		</div>
		<div class="history">
			<ol>
				{#each $gameHistory.history as value, i}
					{#if i == 0}
						<li in:fly="{{ y: 200, duration: 2000 }}" out:fade><button on:click={() => gameHistory.changeStateTo(i)}>Go to game start</button></li>
					{:else}
						<li in:fly="{{ y: 200, duration: 2000 }}" out:fade><button on:click={() => gameHistory.changeStateTo(i)}>Go to move #{i}</button></li>	
					{/if}
				{/each}
			</ol>
		</div>
	</div>
</main>

<style>
	main {
		text-align: center;
		padding: 1em;
		max-width: 240px;
		margin: 0 auto;
	}
	.tic-tac-toe{
		font: 14px "Roboto", sans-serif;
		margin: 20px;
		display: flex;
		flex-direction: row;
	}
	.game-log{
		margin-left: 20px;
	}
	.status{
		margin-bottom: 10px;
	}
	ol{
		padding-left: 30px;
	}

</style>