<script lang="ts">
    import { gamePlay } from "./stores"
    // cells를 여기 binding해서 value로 바꿔줘야 밑에서 사용가능할듯!!
    // cell 정보는 어차피 여기서만 쓰니까 store로 안해도 될듯

    enum State {
        E = 0, O, X      // empty, O, X
    }

    let cells : State[][] = [      // stores the current status of game board cells
        [State.E, State.E, State.E],
        [State.E, State.E, State.E],
        [State.E, State.E, State.E]
    ];

</script>

<div>
    {#each cells as cell_row}
        <div>
            {#each cell_row as cell}
                <button></button>
            {/each}
        </div>
    {/each}
</div>