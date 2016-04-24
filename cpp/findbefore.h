#ifndef XDUTIL_FINDBEFORE_H_
#define XDUTIL_FINDBEFORE_H_

#include <functional>

namespace XDUtil {

/**
 * @brief  same ase find_before but use predicate instead
 *
 */
template <typename ForwardIterator, typename Pred>
ForwardIterator find_before_if(ForwardIterator first, ForwardIterator last,
                               Pred pred) {
    if (first == last) {
        return first;
    }

    ForwardIterator next(first);
    ++next;
    while (next != last && !pred(*next)) {
        ++next;
        ++first;
    }
    return first;
}

/**
 * @brief  find the element before the one equal to val.
 *         this is very useful when operate with std::forwoard_list.
 *         you only need ForwardIterator to make this function work
 *
 * @returns   first match if find, last otherwise
 */
template <typename ForwardIterator, typename T>
ForwardIterator find_before(ForwardIterator first, ForwardIterator last,
                            const T& val) {
    find_before_if(first, last,
                   std::bind(std::equal_to<T>(), std::placeholders::_1, val));
}
}

#endif /* end of include guard: XDUTIL_FINDBEFORE_H_ */
