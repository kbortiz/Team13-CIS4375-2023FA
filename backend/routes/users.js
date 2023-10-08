const express = require('express')
const router = express.Router()

const org = process.env.ORG

// importing data model schemas
const { orgs, users } = require('../models/models')

//GET user by role as a parameter
router.get('/users/:role', async (req, res) => {
  const role = req.params.role;
  const user = await users.findOne({ role: role }).exec();//findOne method to find a user given a role
  if (user) {
    res.status(200).json(user);//and send a user as JSON response
  } else {
    res.status(404).send(`User not found`);
  }
});

// Any other operations for users not necessary
module.exports = router