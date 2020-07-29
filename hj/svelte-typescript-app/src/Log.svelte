<script lang="ts">
    import { gameLog, State, logStatus } from "./stores"

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
                <button on:click={revertLog} id="log_{i}">
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
        width: 160px;
        padding: auto;
        border: 0px;
        border-radius: 5px;
        background: #8ec0fa;
        text-align: center;
        color: rgba(0, 0, 0, 1)
    }

    #log-view {
        margin: 25px;
        display: flex;
        margin: 0px;
    }

    ul {
        list-style: none;

        font-size: 13px;
    }
</style>