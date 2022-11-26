<template>
    <div class="container">
        <div class="columns is-multiline">
            <img src="@/assets/newplayer.png" width="212" height="86px">
            <div class="column is-12">
                <form @submit.prevent="submitForm">
                    <div class="field">
                        <label>Name</label>
                        <div class="control">
                            <input type="text" class="input" v-model="name">
                        </div>
                    </div>
                    <div class="field">
                        <label>Email</label>
                        <div class="control">
                            <input type="email" class="input" v-model="email">
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
        name: 'AddUser',
        data() { 
            return { 
                name: '',
                leads: [],
                email: '',
            }
        },
        mounted() { 
            this.getLeads()
        },
        methods: { 
            async submitForm() { 
                this.$store.commit('setIsLoading', true)
                const lead = { 
                    player: this.player,
                    name: this.name,
                    email: this.email,
                }
                await axios
                    .post('/api/v1/user/', lead)
                    .then(response => { 
                        console.log(response)
                        this.$router.push('/dashboard/players')
                    })
                    .catch(error => { 
                        console.log(error)
                    })
                this.$store.commit('setIsLoading', false)
            },
            async getLeads() { 
                this.$store.commit('setIsLoading', true)
                axios
                    .get('/api/v1/user/')
                    .then(response => { 
                        this.leads = response.data
                    })
                    .catch(error => { 
                        console.log(error)
                    })
                this.$store.commit('setIsLoading', false)
            }
        }
    }
</script>