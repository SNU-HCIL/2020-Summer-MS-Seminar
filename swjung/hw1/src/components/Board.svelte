<script lang="ts">
    import Square from './Square.svelte'
    import { afterUpdate , beforeUpdate } from 'svelte'

    
    let status: string = 'Next player : X';
    let player: string = 'X';
    export let squares: Array<string> = Array(9).fill('');
    export let xIsNext: boolean = true;

</script>

<style>
    .board-row:after {
        clear: both;
        content: '';
        display: table;
    }
    .status {
        margin-bottom: 10px;
    }
</style>

<div class="board-row">
    {#each squares.slice(0, 3) as sq, i}
        <Square value={sq} index={i} on:click/>
    {/each}
</div>
<div class="board-row">
    {#each squares.slice(3, 6) as sq, i}
        <Square value={sq} index={i + 3} on:click/>
    {/each}
</div>
<div class="board-row">
    {#each squares.slice(6, 9) as sq, i}
        <Square value={sq} index={i + 6} on:click/>
    {/each}
</div>
