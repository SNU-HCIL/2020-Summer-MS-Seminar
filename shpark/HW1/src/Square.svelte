<script lang="ts">
    import { fly } from 'svelte/transition';


    export let value: string;
    export let onClick;

</script>

<style>
  .square {
    float: left;
    flex: 1 0 25%;
    width: 70px;
    height: 70px;
    background-color: whitesmoke;
    border: 1px solid gray;
    margin: 5px;
    padding: 5px;
    font-size: 20px;
    text-align: center;
  }

  .square:hover {
    background-color: #ffd4cc;
    border: 2px solid #ff3e00;
  }

  .OX {
    margin: 0px
  }
</style>

    <button class="square" on:click={onClick}>
    {#if value == undefined}
        <p class="OX" in:fly="{{ y: 20, duration: 500 }}">
            {''}
        </p>
    {:else}
        <p class="OX" transition:fly="{{ y: 20, duration: 500 }}">
            {value}
        </p>
    {/if}
    </button>
