use std::ops::Deref;

struct Inner<T> {
    refcount: usize,
    data: T
}

pub struct MyRc<T> {
    inner: *mut Inner<T>
}

impl<T> MyRc<T> {
    pub fn new(value: T) -> Self {
        MyRc { inner: Box::into_raw(Box::new(Inner { refcount: 1, data: value })) }
    }
}

impl<T> Clone for MyRc<T> {
    fn clone(&self) -> Self {
        // Safety
        //
        // Safe because:
        // - `self.inner` is assumed to point to a valid `Inner<T>`.
        // - The refcount is incremented to reflect the creation of a new MyRc handle,
        //   ensuring that the Inner data is not prematurely deallocated.
        // - This operation must be wrapped in a memory fence or use atomic operations
        //   if MyRc is intended to be used in a multi-threaded context.
        unsafe { (*self.inner).refcount += 1 }
        MyRc { inner: self.inner }
    }
}

impl<T> Drop for MyRc<T> {
    fn drop(&mut self) {
        // # Safety
        //
        // Safe because:
        // - We decrement the refcount and only deallocate when it reaches 0,
        //   ensuring no other instances are still using it.
        // - `Box::from_raw` is called to properly deallocate the Inner when refcount is 0,
        //   which prevents memory leaks and respects Rust's ownership rules.
        unsafe {
            (*self.inner).refcount -= 1;

            if (*self.inner).refcount == 0 { let _ = Box::from_raw(self.inner); }
        }
    }
}

impl<T> Deref for MyRc<T> {
    type Target = T;

    fn deref(&self) -> &T {
        // Safety
        //
        // Safe because:
        // - `self.inner` is assumed to always point to a valid Inner<T>.
        // - Dereferencing to &T is safe as long as Inner is not freed, which is
        //   guaranteed by the refcount mechanism in MyRc.
        unsafe { &(*self.inner).data }
    }
}
