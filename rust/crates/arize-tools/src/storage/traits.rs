//! MemoryBackend trait for all storage backends.

use arize_core::{ArizeError, RetrievalResult};
use serde_json::Value;

pub trait MemoryBackend: Send + Sync {
    fn backend_id(&self) -> &str;
    fn store(
        &self,
        content: &str,
        source: &str,
        metadata: Option<&Value>,
    ) -> Result<String, ArizeError>;
    fn retrieve(
        &self,
        query: &str,
        top_k: usize,
    ) -> Result<Vec<RetrievalResult>, ArizeError>;
    fn delete(&self, doc_id: &str) -> Result<bool, ArizeError>;
    fn clear(&self) -> Result<(), ArizeError>;
    fn count(&self) -> Result<usize, ArizeError>;
}
