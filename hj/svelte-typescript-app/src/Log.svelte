<script lang="ts">
    import { gameLog, State } from "./stores"

    let test_gameLog = [
        [[0, 0, 0],
         [0, 1, 0],
         [0, 0, 0]],
        [[0, 0, 0],
         [0, 1, 0],
         [0, 2, 0]],
        [[0, 0, 0],
         [0, 1, 0],
         [0, 2, 1]],
    ];

</script>

<div id="log-view">
    <ul>
        {#each test_gameLog as log, i}
            <li>
                <button>
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