<script lang="ts">
  import { createEventDispatcher } from 'svelte';
  import { fade } from 'svelte/transition';

  export let state: String;
  export let index: number;

  let memory: String = null;

  function remember(state, index) {
    if (state[index] && memory !== state[index]) {
      memory = state[index];
      return state[index];
    }
    else if (memory) return memory;
    else return '';
  }

  const dispatch = createEventDispatcher();
  
  function click() {
    dispatch('message', {
      index: index
    });
  }
</script>

<style>
  .square {
    background: #fff;
    border: 1px solid #999;
    float: left;
    font-size: 24px;
    font-weight: bold;
    line-height: 34px;
    height: 34px;
    margin-right: -1px;
    margin-top: -1px;
    padding: 0;
    text-align: center;
    width: 34px;
    transition: background-color 0.5s;
  }

  .square:focus {
    outline: none;
    background: #ddd;
  }

  .before {
    opacity: 0%;
    transition: opacity 0.5s;
  }

  .after {
    opacity: 100%;
    transition: opacity 0.5s;
  }
</style>

<button class="square" on:click={click}>
  <div class={state[index] ? "after" : "before"}>
  { remember(state, index) }
  </div>
</button>