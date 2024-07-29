package com.google.firebase.arjunrajput.recommendations.adapters

import androidx.fragment.app.Fragment
import androidx.viewpager2.adapter.FragmentStateAdapter
import com.google.firebase.arjunrajput.recommendations.MovieListFragment
import com.google.firebase.arjunrajput.recommendations.LikedMoviesFragment
import com.google.firebase.arjunrajput.recommendations.RecommendationsFragment

const val MOVIE_LIST_PAGE_INDEX = 0
const val LIKED_MOVIES_PAGE_INDEX = 1
const val RECOMMENDED_MOVIES_PAGE_INDEX = 2

class FireFlixPagerAdapter(fragment: Fragment) : FragmentStateAdapter(fragment) {


    private val tabFragmentsCreators: Map<Int, () -> Fragment> = mapOf(
        MOVIE_LIST_PAGE_INDEX to { MovieListFragment() },
        LIKED_MOVIES_PAGE_INDEX to { LikedMoviesFragment() },
        RECOMMENDED_MOVIES_PAGE_INDEX to { RecommendationsFragment() }
    )

    override fun getItemCount() = tabFragmentsCreators.size

    override fun createFragment(position: Int): Fragment {
        return tabFragmentsCreators[position]?.invoke() ?: throw IndexOutOfBoundsException()
    }
}