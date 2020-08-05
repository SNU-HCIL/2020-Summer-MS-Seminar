<script lang="ts">
    import { gameLog, State, logStatus } from "./stores"
    import { scale } from "svelte/transition"

    let logs : any;
    gameLog.subscribe(v => { logs = v });

    function revertLog() {
        let logNum : number = parseInt(this.id[4]);
        logStatus.set(logNum);
    }
    

</script>

<div id="log-view">
    <ul>
        {#each logs as log, i}
            <li>
                <button on:click={revertLog} id="log_{i}" transition:scale>
                    {#if i === 0}
                        Go to game start
                    {:else}
                        Go to move #{i}
                    {/if}
                </button>
            </li>
        {/each}
    </ul>
</div>

<style>
    button {
        margin: 3px;
        width: 200px;
        padding: auto;
        border: 0px;
        border-radius: 5px;
        background: #8ec0fa;
        text-align: center;
        color: rgba(0, 0, 0, 1);
        cursor: pointer;
    }

    #log-view {
        margin: 25px;
        display: flex;
        margin: 0px;
    }

    ul {
        list-style: none;
        font-size: 13px;
        margin-left: 20px;
        margin-right: 20px;
        padding: 0px;
    }
</style>