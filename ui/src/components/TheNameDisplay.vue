<script setup>
import { ref } from 'vue';
defineProps(['name', 'build', 'isNewPinesamAvailable', 'isNewBuildAvailable']);
const isNameHidden = ref(true);
</script>
<template>
  <div class="new-available restore-click">
    <a v-if="isNewPinesamAvailable" href="https://github.com/builder555/PineSAM/releases/latest" target="_blank">New PineSAM Available</a>
    &nbsp;<a v-if="isNewBuildAvailable" href="https://github.com/Ralim/IronOS/releases/latest" target="_blank">New IronOS Available</a>
  </div>
  <h1 class="title">
    <a class="restore-click" @click="isNameHidden = !isNameHidden || !name">
      <span class="accent" v-if="isNameHidden">PineSAM</span>
      <span class="accent small" v-else>
        {{ name }} <span class="smaller" v-if="build">(build {{ build }})</span>
      </span>
    </a>
  </h1>
</template>
<style scoped>
.refresh-button {
  font-size: 1.2rem;
  margin: 0 0 0 0.5rem;
}
h1 {
  font-family: 'Righteous', "Segoe UI", Roboto, Oxygen, Ubuntu, Cantarell, "Helvetica Neue", Helvetica, Arial, sans-serif;
}
.small {
  font-size: 0.8em;
}
.smaller {
  font-size: 0.6em;
}
.new-available {
  position:absolute;
  font-size: 0.7rem;
  font-family: inherit;
  top:3rem;
  z-index:1;
}
</style>
