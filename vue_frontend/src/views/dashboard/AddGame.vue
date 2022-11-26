<template>
    <div class="container">
        <div class="columns is-multiline">
        <img src="@/assets/newgame.png" width="212" height="86px">
            <div class="column is-12">
                <form @submit.prevent="submitForm">
                    <div class="field">
                        <label>Select Players</label>
                        <div class="control">
                            <div class="select is-multiple">
                                <select multiple size="4" v-model="player">
                                    <option v-for="item , key in game" :value="item.id">{{item.name}}</option>
                                </select>
                            </div>
                        </div>
                    </div>
                    <div class="field">
                        <div class="control">
                            <button class="button is-dark">Submit</button>
                        </div>
                    </div>
                </form>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
    export default { 
        name: 'AddGame',
        data() { 
            return { 
                player: '',
                game: [],
            }
        },
        mounted() { 
            this.getAddGame()
        },
        methods: { 
            async submitForm() { 
                this.$store.commit('setIsLoading', true)
                const game = { 
                    player: this.player,
                }
                await axios
                    .post('/api/v1/games/', game)
                    .then(response => { 
                        console.log(response)
                        this.$router.push('/dashboard/games')
                    })
                    .catch(error => { 
                        console.log(error)
                    })
                this.$store.commit('setIsLoading', false)
            },
            async getAddGame() { 
                this.$store.commit('setIsLoading', true)
                axios
                    .get('/api/v1/user/')
                    .then(response => { 
                        this.game = response.data
                    })
                    .catch(error => { 
                        console.log(error)
                    })
                this.$store.commit('setIsLoading', false)
            }
        }
    }
</script>