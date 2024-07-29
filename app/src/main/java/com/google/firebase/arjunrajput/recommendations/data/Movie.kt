
package com.google.firebase.arjunrajput.recommendations.data

data class Movie(
    val id: Int,
    val title: String,
    val genres: List<String>,
    val count: Int,
    var liked: Boolean
)